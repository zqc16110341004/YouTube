from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import yt_dlp
import os
import asyncio
import json
from datetime import datetime, timedelta
import humanize

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 存储下载视频的信息
VIDEOS_DIR = "static/videos"
VIDEOS_INFO_FILE = "static/videos_info.json"

# 确保必要的目录存在
os.makedirs(VIDEOS_DIR, exist_ok=True)

# 读取已下载视频信息
def load_videos_info():
    if os.path.exists(VIDEOS_INFO_FILE):
        with open(VIDEOS_INFO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 保存视频信息
def save_videos_info(videos_info):
    with open(VIDEOS_INFO_FILE, 'w', encoding='utf-8') as f:
        json.dump(videos_info, f, ensure_ascii=False, indent=2)

@app.get("/")
async def home(request: Request):
    videos = load_videos_info()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "videos": videos}
    )

@app.post("/download")
async def download_video(url: str = Form(...)):
    try:
        # 配置yt-dlp选项
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(VIDEOS_DIR, '%(title)s.%(ext)s'),
            'quiet': True,
        }
        
        # 首先获取视频信息
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # 准备视频信息
            video_info = {
                'title': info['title'],
                'duration': str(timedelta(seconds=info['duration'])),
                'author': info['uploader'],
                'description': info.get('description', '')[:200] + '...',
                'url': url,
                'thumbnail': info.get('thumbnail', ''),
                'download_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'local_path': os.path.join(VIDEOS_DIR, f"{info['title']}.{info['ext']}")
            }
            
            # 下载视频
            ydl.download([url])
            
            # 获取文件大小
            file_size = os.path.getsize(video_info['local_path'])
            video_info['file_size'] = humanize.naturalsize(file_size)
            
            # 更新视频列表
            videos_info = load_videos_info()
            videos_info.append(video_info)
            save_videos_info(videos_info)
            
            return JSONResponse({"status": "success", "video_info": video_info})
            
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"status": "error", "message": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 