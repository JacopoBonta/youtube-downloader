# youtube-downloader

youtube-downloader is a service that allow to download and eventually convert downloaded videos to mp3 files from youtube video links. It is designed to live in a docker container and to be compatible with a microservice architecture.
The service is written in python and exposes its functionalities through a RESTful HTTP API.

## Usage
```bash
docker run -d -v /local/path/:/app/data -p 3000:80 m0-youtube-downloader
```

## Enpoints

* **`/download [POST]`**

  Download a video from youtube. The downloaded video will be available in the mounted volume. You can choose to convert the downloaded video in to a mp3 music file.

  Payload:
  ```
  {
    video_url: 'https://youtube.com/' # the url of the video you want to download
    convert:  true # true if you want to convert the video to mp3 (not yet implemented)
  }
  ```

* **`/status [GET]`**

  Get the status of the downloads. A download can be in one of three different statuses: PENDING, READY, ERROR.

* **`/status/<int:id> [GET]`**

  Get the status of a single download by its id. A download can be in one of three different statuses: PENDING, READY, ERROR.