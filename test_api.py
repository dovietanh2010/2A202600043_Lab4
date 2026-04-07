import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env
load_dotenv()

# Khởi tạo LLM (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

# Gọi model
response = llm.invoke("Xin chào?")

print(response.content)