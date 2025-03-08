import yt_dlp
import os
from pathlib import Path

# 自定义下载路径
download_path = os.path.join("D:", "Youtube下载文件夹")  # 使用 os.path.join 来处理路径

# 确保下载文件夹存在
os.makedirs(download_path, exist_ok=True)

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 配置yt-dlp选项
ydl_opts = {
    'format': 'best',  # 下载最佳质量
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # 设置输出模板
    'ignoreerrors': True,  # 忽略错误继续下载
}

def download_videos():
    # 读取url文件（放在当前脚本目录下）
    url_file_path = os.path.join(current_dir, "youtube下载输入链接_可写入多行.txt")
    
    if not os.path.exists(url_file_path):
        # 创建示例文件
        with open(url_file_path, "w", encoding="utf-8") as f:
            f.write("# 在下方输入YouTube视频链接，每行一个链接\n")
            f.write("# 示例1：https://www.youtube.com/watch?v=xxxxx\n")
            f.write("# 示例2：https://www.youtube.com/watch?v=yyyyy\n")
            f.write("# 示例3：https://www.youtube.com/watch?v=zzzzz\n")
        print(f"已创建链接输入文件：{url_file_path}")
        print("请在文件中添加要下载的视频链接（每行一个）")
        input("添加完成后按回车键继续...")
        return

    # 读取URL列表
    with open(url_file_path, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not urls:
        print("未找到有效的YouTube链接，请在youtube_urls.txt中添加链接")
        return

    print(f"找到 {len(urls)} 个视频链接")
    print(f"下载路径: {download_path}")
    print("开始下载...")
    
    # 下载视频
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                print(f"\n正在下载: {url}")
                ydl.download([url])
            except Exception as e:
                print(f"下载失败: {str(e)}")

    print("\n所有下载任务完成！")
    input("按回车键退出...")

if __name__ == "__main__":
    download_videos()
