from dotenv import load_dotenv
load_dotenv()
from flask import Flask, make_response, jsonify, request, abort
from src.video_downloader import download_and_save_video
import os
import time

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def invalid_parameters(error):
    return make_response(jsonify({'error': 'Invalid parameter'}), 400)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal server error'}), 500)

@app.route('/download', methods=['POST'])
def download(urlstr="", convert=False):

    downloads_path  =   os.getenv('DOWNLOAD_PATH')
    
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')