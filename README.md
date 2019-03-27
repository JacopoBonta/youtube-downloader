# youtube-downloader

youtube-downloader is a service that allow to download and eventually convert downloaded videos to mp3 files from youtube video links. It is designed to live in a docker container and to be compatible with a microservice architecture.
The service is written in python and exposes its functionalities through a RESTful HTTP API.
A database its also used to store videos and audio metadata.