import pytube

def download_and_save_video(url, path, convert):
    yt  =   pytube.YouTube(url)

    videos  =   yt.streams.first()

    videos.download(path)