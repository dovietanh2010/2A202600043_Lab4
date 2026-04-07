# TravelBuddy - Test Cases

## Test case 1: Chưa biết đi đâu

**Bạn**: 
Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu


**TravelBuddy:** 
Chào bạn! Rất vui được hỗ trợ bạn lên kế hoạch du lịch. Để mình có thể tư vấn tốt nhất, bạn có thể cho mình biết một vài thông tin sau không:

1.  **Bạn muốn đi trong nước hay nước ngoài?**
2.  **Bạn dự định đi vào khoảng thời gian nào?** (Ví dụ: cuối tuần này, tháng sau, mùa hè...)
3.  **Ngân sách dự kiến của bạn là khoảng bao nhiêu?** (Ước lượng thôi cũng được, để mình dễ hình dung nhé)
4.  **Bạn thích kiểu du lịch nào?** (Ví dụ: nghỉ dưỡng, khám phá, biển, núi, thành phố...)

Càng có nhiều thông tin, mình càng dễ dàng tìm được điểm đến ưng ý cho bạn đó! 😊

## Test case 2: Tìm chuyến bay từ Hà Nội đi Đà Nẵng

**Bạn:**  
Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

**TravelBuddy:**  

[TOOL] Gọi: search_flights | Args: {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}

Tuyệt vời! TravelBuddy đã tìm thấy một vài lựa chọn chuyến bay từ Hà Nội đi Đà Nẵng cho bạn đây:

* **Vietnam Airlines (hạng phổ thông):** Khởi hành 06:00, đến 07:20, giá 1.450.000đ
* **Vietnam Airlines (hạng thương gia):** Khởi hành 14:00, đến 15:20, giá 2.800.000đ
* **VietJet Air (hạng phổ thông):** Khởi hành 08:30, đến 09:50, giá 890.000đ
* **Bamboo Airways (hạng phổ thông):** Khởi hành 11:00, đến 12:20, giá 1.200.000đ

Bạn thấy sao, có chuyến nào ưng ý không? Nếu muốn, mình có thể tìm thêm khách sạn ở Đà Nẵng hoặc tính toán ngân sách cho chuyến đi của bạn nhé!

---

## Test case 3: Tư vấn đi Phú Quốc 2 đêm, budget 5 triệu

**Bạn:**  
Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

**TravelBuddy:**  

[TOOL] Gọi: search_flights | Args: {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}

[TOOL] Gọi: search_hotels | Args: {'city': 'Phú Quốc', 'max_price_per_night': 1950000}

[TOOL] Gọi: calculate_budget | Args: {'total_budget': 5000000, 'expenses': 'vé máy bay:1100000, khách sạn:1600000'}

Chào bạn, với ngân sách 5 triệu đi Phú Quốc 2 đêm từ Hà Nội, mình đã tìm được vài lựa chọn rất ổn đây:

**Chuyến bay:**  
* Bạn có thể chọn VietJet Air chuyến 16:00-18:15 với giá 1.100.000đ. Giá này khá tốt đó!

**Khách sạn:**  
* Mình gợi ý bạn tham khảo Lahana Resort (3 sao) ở Dương Đông, giá 800.000đ/đêm. Khách sạn này có rating 4.0 và nằm ở khu trung tâm, khá tiện lợi. Tổng 2 đêm sẽ là 1.600.000đ.
* Nếu muốn tiết kiệm hơn, 9Station Hostel (2 sao) cũng là một lựa chọn với giá chỉ 200.000đ/đêm và rating 4.5.

**Tổng chi phí ước tính:**  
* Vé máy bay: 1.100.000đ  
* Khách sạn (Lahana Resort): 1.600.000đ  
* Tổng cộng: 2.700.000đ  
* Bạn còn dư 2.300.000đ để chi tiêu ăn uống, đi lại và vui chơi đó!

**Gợi ý thêm:**  
Với số tiền còn lại, bạn có thể dành để đi tour 4 đảo, thăm VinWonders hoặc Grand World, hoặc đơn giản là thưởng thức hải sản tươi ngon ở chợ đêm Dinh Cậu. Đừng quên thử bún quậy, gỏi cá trích nhé, đặc sản Phú Quốc đó!

Bạn thấy sao về lịch trình này? Có cần mình tìm thêm lựa chọn nào khác không?

---

## Test case 4: Đặt khách sạn

**Bạn**: Tôi muốn đặt khách sạn 

**TravelBuddy:** Chào bạn, bạn muốn đặt khách sạn ở đâu và ngân sách của bạn cho mỗi đêm là bao nhiêu?

---

## Test case 5: Hỏi bài tập Python về Linked list

**Bạn:**  
Giải giúp tôi bài tập lập trình Python về Linked list

**TravelBuddy:**  
Chào bạn, mình là trợ lý du lịch của TravelBuddy, chuyên về du lịch Việt Nam thôi. Mình không thể giúp bạn giải bài tập lập trình được. Nếu bạn cần tư vấn về chuyến đi, đặt vé máy bay hay khách sạn, cứ hỏi mình nhé!