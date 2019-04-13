import os
from main import app, store
from src.video_downloader import download_and_save_video
from flask import request, jsonify, abort

@app.route('/download', methods=['POST'])
def download(urlstr="", convert=False):

    downloads_path  =   os.getenv('DOWNLOAD_PATH')
    
    if ('video_url' not in request.json) or ('convert' not in request.json):
        abort(400)

    video_url   =   request.json['video_url']
    convert     =   request.json['convert']

    try:
        download_and_save_video(video_url, downloads_path, convert)
    except Exception as e:
        print('download exception', e)
        abort(500)
    else:
        return jsonify({'result': True})