import uvicorn
import webbrowser
import time
import threading

def open_browser():
    # 等待服务器启动
    time.sleep(2)
    # 打开默认浏览器
    webbrowser.open('http://localhost:8000')

if __name__ == "__main__":
    print("正在启动 YouTube 视频下载器...")
    print("服务器启动后将自动打开浏览器...")
    
    # 在新线程中启动浏览器
    threading.Thread(target=open_browser).start()
    
    # 启动服务器
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 