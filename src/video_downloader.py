import pytube
import threading
import time
from src.store import Store

def _download_and_save_video(url, path, convert):

  store = Store()

  download_id = store.insert_download(url, 'PENDING')  

  t0  =   time.time()

  yt      =   pytube.YouTube(url)
  videos  =   yt.streams.first()
  videos.download(path)

  t1  =   time.time()
  
  store.query('''UPDATE downloads
                  SET status = ?, time = ?
                  WHERE id = ?
              ''', ('READY', str(t1 - t0), download_id))

def download_and_save_video(url, path, convert):
  thread        = threading.Thread(target=_download_and_save_video, args=(url, path, convert))
  thread.daemon = True
  thread.start()