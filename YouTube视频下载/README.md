# YouTube 视频下载器

一个简单易用的 YouTube 视频下载工具，基于 Python FastAPI 和 yt-dlp 开发。

## 功能特点

- 支持下载 YouTube 视频
- 美观的用户界面
- 显示下载进度
- 支持视频预览
- 保存下载历史

## 安装步骤

1. 确保已安装 Python 3.8 或更高版本
2. 克隆或下载此项目到本地
3. 在终端中进入项目目录
4. 安装依赖包：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 在终端中进入项目目录
2. 运行以下命令启动应用：
```bash
python run.py
```
3. 在浏览器中访问：http://localhost:8000
4. 将 YouTube 视频链接粘贴到输入框，点击下载按钮

## 注意事项

- 确保有足够的磁盘空间
- 需要稳定的网络连接
- 下载的视频保存在 `static/videos` 目录下
- 视频信息保存在 `static/videos_info.json` 文件中

## 常见问题

Q: 如何更改下载视频的保存位置？
A: 修改 `main.py` 中的 `VIDEOS_DIR` 变量值即可。

Q: 支持哪些视频格式？
A: 支持 YouTube 上的所有常见视频格式，默认下载最高质量版本。

## 技术支持

如有问题，请提交 Issue 或联系开发者。 