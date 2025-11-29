import gradio as gr
from app.engine import CosmicEngine

# Khởi tạo engine (Back-end)
engine = CosmicEngine()

def fn_generate(prompt, neg_prompt, steps, scale, width, height):
    if not prompt:
        return None, "Vui lòng nhập mô tả ảnh!"
    
    try:
        image, en_prompt = engine.generate(prompt, neg_prompt, steps, scale, height, width)
        return image, f"Đã dịch sang: {en_prompt}"
    except Exception as e:
        return None, f"Lỗi: {str(e)}"

# Custom CSS để giao diện đẹp hơn
custom_css = """
#gen-btn {
    background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
    color: white;
    border: none;
}
#gen-btn:hover {
    transform: scale(1.02);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
"""

def create_ui():
    with gr.Blocks(title="CosmicMan Generator", css=custom_css, theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🌌 CosmicMan Human Generator
            Nhập mô tả.
            """
        )
        
        with gr.Row():
            # Cột bên trái: Cài đặt
            with gr.Column(scale=1, variant="panel"):
                prompt_input = gr.Textbox(
                    label="Mô tả hình ảnh",
                    placeholder="Ví dụ: Một cô gái trẻ đang cười dưới nắng...",
                    lines=3
                )
                neg_input = gr.Textbox(
                    label="Những thứ không muốn xuất hiện (Negative Prompt)",
                    value="",
                    lines=2
                )
                
                with gr.Accordion("Cài đặt nâng cao", open=False):
                    with gr.Row():
                        width = gr.Slider(label="Chiều rộng", minimum=512, maximum=1024, value=1024, step=64)
                        height = gr.Slider(label="Chiều cao", minimum=512, maximum=1024, value=1024, step=64)
                    
                    steps = gr.Slider(label="Số bước (Steps)", minimum=10, maximum=100, value=30, step=1)
                    scale = gr.Slider(label="Độ bám sát văn bản (Guidance Scale)", minimum=1, maximum=20, value=7.5, step=0.5)

                generate_btn = gr.Button("🚀 Tạo hình ảnh", elem_id="gen-btn", size="lg")
                
            # Cột bên phải: Kết quả
            with gr.Column(scale=2):
                output_image = gr.Image(label="Kết quả", type="pil", interactive=False)
                status_text = gr.Markdown(label="Trạng thái")

        # Kết nối sự kiện
        generate_btn.click(
            fn=fn_generate,
            inputs=[prompt_input, neg_input, steps, scale, width, height],
            outputs=[output_image, status_text]
        )
        
    return demo