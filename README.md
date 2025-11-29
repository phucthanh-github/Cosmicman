# 🌌 Cosmicman - Text-to-Human-Images Website

**Cosmicman** là một ứng dụng web AI cho phép tạo hình ảnh con người chất lượng cao từ văn bản mô tả tiếng Việt hoặc tiếng Anh, đặc biệt hiệu quả cho các văn bản mô tả nhiều chi tiết và phức tạp. Dự án sử dụng mô hình **CosmicMan-SD** (một mô hình được huấn luyện chuyên biệt cho việc tạo dựng hình ảnh con người từ văn bản, sử dụng khung huấn luyện thông minh Daring) kết hợp với mô hình dịch thuật **VinAI Translate** để cho phép người dùng có thể sử dụng ngay cả trên văn bản tiếng Việt.
![Demo](demo.png)
<br>
*(prompt: Một bức ảnh chân dung chụp cận cảnh một phụ nữ da trắng trưởng thành, thân hình cân đối, tóc vàng gợn sóng dài ngang ngực, mặc một chiếc váy lụa ngắn tay hoa văn, nền tường trắng.)*

## ✨ Tính năng chính
- 🇻🇳 **Hỗ trợ Tiếng Việt:** Nhập prompt trực tiếp bằng tiếng Việt, hệ thống tự động dịch sang tiếng Anh chuẩn cho model.
- 👩‍🦰 **Chuyên biệt về con người:** Sử dụng CosmicMan-SD, tối ưu hóa cho việc tạo chi tiết khuôn mặt, cơ thể và dáng người.
- 🎛 **Giao diện trực quan:** Tích hợp thành trượt điều chỉnh kích thước ảnh, số bước (steps) và độ bám sát văn bản (guidance scale).
- 🚀 **Modular Design:** Cấu trúc code tách biệt giữa Engine xử lý và Giao diện (UI), dễ dàng mở rộng.

## 🛠 Yêu cầu hệ thống
- **Python:** 3.8 trở lên.
- **GPU:** Khuyên dùng NVIDIA GPU (VRAM >= 6GB) để có tốc độ tốt nhất. Có thể chạy trên CPU nhưng sẽ chậm.
- **Ổ cứng:** Còn trống khoảng 10GB để tải các models.

## ⚙️ Hướng dẫn cài đặt

### 1. Clone dự án
```bash
git clone [https://github.com/username-cua-ban/CosmicGen.git](https://github.com/username-cua-ban/CosmicGen.git)
cd CosmicGen
```
### 2. Cài đặt môi trường 
```bash
pip install -r requirements.txt
```
Lưu ý: nên sử dụng môi trường ảo
#### Đối với Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
#### Đối với macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Khởi chạy website
```bash
python main.py
```
