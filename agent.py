from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM + Tools
tools_list = [search_flights, search_hotels, calculate_budget]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    max_retries=3,
)

llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    
    # Luôn đảm bảo có SystemMessage đầu tiên
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)

    # === LOGGING TOOL CALL ===
    tool_calls = getattr(response, 'tool_calls', []) or []
    
    if tool_calls:
        for tc in tool_calls:
            print(f"[TOOL] Gọi: {tc['name']} | Args: {tc['args']}")
    else:
        if isinstance(response.content, list):
            for part in response.content:
                if isinstance(part, dict) and part.get("type") == "functionCall":
                    name = part.get("functionCall", {}).get("name")
                    args = part.get("functionCall", {}).get("args")
                    print(f"[TOOL] Gọi (từ content): {name} | Args: {args}")
    
    print("[TOOL] Không gọi tool nào, trả lời trực tiếp" if not tool_calls and not (isinstance(response.content, list) and any(p.get("type") == "functionCall") for p in response.content if isinstance(p, dict)) else "")

    return {"messages": [response]}

# 5. Tool Node
tool_node = ToolNode(tools_list)

# 6. Xây dựng Graph
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()

# 7. Extract content
def extract_content(message):
    if hasattr(message, 'content'):
        content = message.content
        
        if isinstance(content, str):
            return content.strip()
        
        if isinstance(content, list):
            texts = []
            for item in content:
                if isinstance(item, dict):
                    if item.get('type') == 'text':
                        texts.append(item.get('text', ''))
                    elif item.get('type') == 'functionCall':
                        continue
                elif isinstance(item, str):
                    texts.append(item)
            return '\n'.join(texts).strip() if texts else str(content)
    
    return str(message.content) if hasattr(message, 'content') else str(message)

# 8. Chat loop
if __name__ == "__main__":
    print("=" * 70)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print("  Nhập 'quit' để thoát")
    print("=" * 70)
    
    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Tạm biệt! Chúc bạn có chuyến đi vui vẻ!")
            break
        
        print("\nTravelBuddy đang suy nghĩ...")
        try:
            result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
            
            final_message = result["messages"][-1]
            content = extract_content(final_message)
            
            print(f"\nTravelBuddy: {content}")
            
        except Exception as e:
            print(f"\nLỗi: {e}")