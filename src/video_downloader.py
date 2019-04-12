import pytube
import threading
import time
from src.store import Store

def _download_and_save_video(url, path, convert):

  store = Store()

  download_id = store.add_download(url)

  try:
    print('download started')
    yt      =   pytube.YouTube(url)
    videos  =   yt.streams.first()
    videos.download(path)
  except Exception as e:
    print('download errored')
    print(e)

    store.set_status(download_id, 'DOWNLOAD_ERROR')
    store.log('ERROR', str(e))

  else:
    print('download ended')
    store.set_status(download_id, 'READY')
    store.log('INFO', str(url) + ' download completato')

  finally:
    return 0

def download_and_save_video(url, path, convert):
  print('starting download thread...')
  thread        = threading.Thread(target=_download_and_save_video, args=(url, path, convert))
  thread.daemon = True
  thread.start()