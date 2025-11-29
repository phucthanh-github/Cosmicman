import torch
from diffusers import StableDiffusionPipeline, UNet2DConditionModel, EulerDiscreteScheduler
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class CosmicEngine:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Đang khởi tạo Engine trên thiết bị: {self.device}...")
        
        self.pipe = None
        self.trans_model = None
        self.trans_tokenizer = None
        
        # Tải model ngay khi khởi tạo hoặc có thể lazy load
        self.load_models()

    def load_models(self):
        print("Đang tải mô hình dịch thuật VinAI...")
        trans_model_name = "vinai/vinai-translate-vi2en-v2"
        self.trans_tokenizer = AutoTokenizer.from_pretrained(trans_model_name, src_lang="vi_VN", tgt_lang="en_XX")
        self.trans_model = AutoModelForSeq2SeqLM.from_pretrained(trans_model_name).to(self.device)

        print("Đang tải mô hình CosmicMan-SD...")
        base_path = "runwayml/stable-diffusion-v1-5"
        unet_path = "cosmicman/CosmicMan-SD"

        # Cấu hình model
        unet = UNet2DConditionModel.from_pretrained(unet_path, torch_dtype=torch.float16)
        self.pipe = StableDiffusionPipeline.from_pretrained(
            base_path, 
            unet=unet, 
            torch_dtype=torch.float16, 
            variant="fp16", 
        ).to(self.device)
        
        self.pipe.scheduler = EulerDiscreteScheduler.from_pretrained(
            base_path, 
            subfolder="scheduler", 
            torch_dtype=torch.float16
        )
        print("Hoàn tất tải mô hình!")

    def translate_vi_to_en(self, text):
        if not text:
            return ""
        
        input_ids = self.trans_tokenizer(text, return_tensors="pt").input_ids.to(self.device)
        en_lang_id = self.trans_tokenizer.lang_code_to_id["en_XX"]
        
        output_ids = self.trans_model.generate(
            input_ids,
            max_length=1024,
            early_stopping=True,
            num_beams=5,
            forced_bos_token_id=en_lang_id
        )
        
        return self.trans_tokenizer.decode(output_ids[0], skip_special_tokens=True)

    def generate(self, prompt, negative_prompt, steps, guidance_scale, height=1024, width=1024):
        if self.pipe is None:
            return None, "Mô hình chưa được tải."

        # Dịch prompt
        en_prompt = self.translate_vi_to_en(prompt)
        en_negative = self.translate_vi_to_en(negative_prompt)
        
        print(f"Prompt (VI): {prompt} -> (EN): {en_prompt}")

        # Tạo ảnh
        image = self.pipe(
            prompt=en_prompt,
            negative_prompt=en_negative,
            num_inference_steps=int(steps),
            guidance_scale=float(guidance_scale),
            height=int(height),
            width=int(width)
        ).images[0]

        return image, en_prompt