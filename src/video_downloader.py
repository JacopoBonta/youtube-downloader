import pytube
import threading

def _download_and_save_video(url, path, convert):
  yt      =   pytube.YouTube(url)
  videos  =   yt.streams.first()
  videos.download(path)

def download_and_save_video(url, path, convert):
  thread        = threading.Thread(target=_download_and_save_video, args=(url, path, convert))
  thread.daemon = True
  thread.start()