import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [params, setParams] = useState({
    steps: 30,
    guidance_scale: 7.5,
    width: 512,
    height: 768,
  });

  const handleGenerate = async () => {
    if (!prompt) return alert("Vui lòng nhập mô tả!");
    
    setLoading(true);
    setResult(null);

    try {
      // Gọi API sang Backend Python
      const response = await axios.post('http://127.0.0.1:8000/generate', {
        prompt: prompt,
        negative_prompt: "low quality, blurry, deformed, ugly",
        ...params
      }, {
        timeout: 600000
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Có lỗi xảy ra khi kết nối server!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>🌌 Cosmicman</h1>
        <p>Text To Human Images Model</p>
      </header>

      <div className="main-content">
        {/* Cột trái: Input */}
        <div className="control-panel">
          <div className="form-group">
            <label>Mô tả hình ảnh (Tiếng Việt/Tiếng anh)</label>
            <textarea 
              rows="4" 
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Ví dụ: Một nữ chiến binh mặc giáp bạc..."
            />
          </div>

          <div className="settings">
            <div className="form-group">
              <label>Chiều rộng: {params.width}px</label>
              <input type="range" min="512" max="1024" step="64" 
                value={params.width} 
                onChange={(e) => setParams({...params, width: Number(e.target.value)})}
              />
            </div>
            <div className="form-group">
              <label>Chiều cao: {params.height}px</label>
              <input type="range" min="512" max="1024" step="64" 
                value={params.height} 
                onChange={(e) => setParams({...params, height: Number(e.target.value)})}
              />
            </div>
          </div>

          <button onClick={handleGenerate} disabled={loading} className="gen-btn">
            {loading ? "Đang vẽ..." : "🚀 Tạo hình ảnh"}
          </button>
        </div>

        {/* Cột phải: Kết quả */}
        <div className="preview-panel">
          {result ? (
            <div className="result-card">
              <img 
                src={`data:image/png;base64,${result.image_base64}`} 
                alt="Generated" 
              />
              <p className="caption">Prompt dịch: {result.translated_prompt}</p>
              <a href={`data:image/png;base64,${result.image_base64}`} download="cosmic_gen.png" className="download-link">
                ⬇ Tải ảnh về
              </a>
            </div>
          ) : (
            <div className="placeholder">
              {loading ? <div className="loader"></div> : "Kết quả sẽ hiện ở đây"}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;