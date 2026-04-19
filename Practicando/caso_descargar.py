import yt_dlp

# Descargar un video de YouTube usando yt-dlp
def descargar_video(url):
    opciones = {
        'outtmpl': r'C:\Users\SERGIO\Videos\test\download_videos_phyton\%(title)s.%(ext)s',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

# Ejemplo de uso
url_video = "https://youtube.com/shorts/smW5qDqjSp0?si=ntHXQfyHJTvCwHkA"
descargar_video(url_video)
