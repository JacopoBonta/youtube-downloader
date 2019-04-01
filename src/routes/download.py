import time
import os
from main import app
from src.video_downloader import download_and_save_video
from flask import request, jsonify, abort

@app.route('/download', methods=['POST'])
def download(urlstr="", convert=False):

    downloads_path  =   os.getenv('DOWNLOAD_PATH')

    print('downloads_path', downloads_path)
    
    if 'video_url' not in request.json or 'convert' not in request.json:
        abort(400)

    video_url   =   request.json['video_url']
    convert     =   request.json['convert']

    try:
        print('New download started', video_url)
        t0  =   time.time()
        download_and_save_video(video_url, downloads_path, convert)
        t1  =   time.time()
        print('Download ended', t1 - t0)
    except Exception as e:
        print('download exception', e)
        abort(500)
    else:
        return jsonify({'result': True})