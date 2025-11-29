from app.interface import create_ui
import os

if __name__ == "__main__":
    print("--- Đang khởi động Website CosmicMan ---")
    # Tạo giao diện
    app = create_ui()
    
    # Khởi chạy server
    # share=True sẽ tạo public lin
    # inbrowser=True sẽ tự động mở trình duyệt
    app.queue().launch(share=False, inbrowser=True)