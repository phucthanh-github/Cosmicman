from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.engine import CosmicEngine
import io
import base64

# Khởi tạo App
app = FastAPI(title="CosmicGen API")

# Cấu hình CORS (Để Frontend React gọi được Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong thực tế nên để domain cụ thể
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Khởi tạo Engine AI một lần duy nhất
engine = CosmicEngine()

# Định nghĩa dữ liệu đầu vào (Request Body)
class GenRequest(BaseModel):
    prompt: str
    negative_prompt: str = "low quality, blurry, deformed"
    steps: int = 30
    guidance_scale: float = 7.5
    width: int = 512
    height: int = 768

@app.get("/")
def read_root():
    return {"status": "CosmicGen Backend is running!"}

@app.post("/generate")
def generate_image(req: GenRequest):
    try:
        # Gọi hàm tạo ảnh từ engine
        image, en_prompt = engine.generate(
            req.prompt, 
            req.negative_prompt, 
            req.steps, 
            req.guidance_scale, 
            req.height, 
            req.width
        )
        
        # Chuyển ảnh PIL thành chuỗi Base64 để gửi về Frontend
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return {
            "image_base64": img_str,
            "translated_prompt": en_prompt
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))