# 🌌 Cosmicman - Text-to-Human-Images Website

**Cosmicman** là một ứng dụng web AI cho phép tạo hình ảnh con người chất lượng cao từ văn bản mô tả tiếng Việt hoặc tiếng Anh, đặc biệt hiệu quả cho các văn bản mô tả nhiều chi tiết và phức tạp. Dự án sử dụng mô hình **CosmicMan-SD** (một mô hình được huấn luyện chuyên biệt cho việc tạo dựng hình ảnh con người từ văn bản, sử dụng khung huấn luyện thông minh Daring) kết hợp với mô hình dịch thuật **VinAI Translate** để cho phép người dùng có thể sử dụng ngay cả trên văn bản tiếng Việt.
![Demo](demo.png)
<br>
*(prompt: Một bức ảnh chân dung chụp cận cảnh một phụ nữ da trắng trưởng thành, thân hình cân đối, tóc vàng gợn sóng dài ngang ngực, mặc một chiếc váy lụa ngắn tay hoa văn, nền tường trắng.)*

## ✨ Tính năng chính
- 🇻🇳 **Hỗ trợ Tiếng Việt:** Nhập prompt trực tiếp bằng tiếng Việt, hệ thống tự động dịch sang tiếng Anh chuẩn cho model.
- 👩‍🦰 **Chuyên biệt về con người:** Sử dụng CosmicMan-SD, tối ưu hóa cho việc tạo chi tiết khuôn mặt, cơ thể và dáng người.
- 🎛 **Giao diện trực quan:** Tích hợp thành trượt điều chỉnh kích thước ảnh, số bước (steps) và độ bám sát văn bản (guidance scale).
- 🚀 **Kiến trúc Fullstack**:

    - Backend: FastAPI (Python) mạnh mẽ, xử lý tác vụ AI bất đồng bộ.

    - Frontend: React + Vite (Node.js) cho giao diện hiện đại, phản hồi nhanh.

## 🛠 Yêu cầu hệ thống
- **Python:** 3.8 trở lên.
- **GPU:** Khuyên dùng NVIDIA GPU (VRAM >= 6GB) để có tốc độ tốt nhất. Có thể chạy trên CPU nhưng sẽ chậm.
- **Node.js**: Phiên bản 16+ (Để chạy Frontend React).
- **Ổ cứng:** Còn trống khoảng 10GB để tải các models.

## ⚙️ Hướng dẫn cài đặt
Dự án bao gồm 2 phần: Backend và Frontend. Bạn cần mở 2 cửa sổ Terminal để chạy song song.
### 1. Clone dự án
```bash
git clone [https://github.com/username-cua-ban/CosmicGen.git](https://github.com/username-cua-ban/CosmicGen.git)
cd CosmicGen
```
### 2. Cài đặt Backend (Terminal 1) 
```bash
cd backend

# Tạo môi trường ảo (Windows)
python -m venv venv
.\venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt
```

### 3. Cài đặt Frontend (Terminal 2)
```bash
cd frontend

# Cài đặt các gói Node.js 
npm install
```
## Khởi chạy dự án
Bạn bắt buộc phải duy trì cả 2 Terminal hoạt động cùng lúc.
### 1. Terminal 1: Khởi chạy Server AI (Backend)
``` bash
python -m uvicorn main:app --reload
```
### 2. Khởi chạy Giao diện Web (Frontend)
``` bash
npm run dev
```
Sau khi chạy, truy cập trình duyệt tại địa chỉ hiện ra (thường là): http://localhost:5173
