from main import app, store
from flask import request, jsonify, abort

@app.route('/status', methods=['GET'])
def status_list():
  
  downloads_c  = store.query('SELECT * FROM downloads')
  statuses  = []

  for download in downloads_c:
    statuses.append({
      'status'    : download[3],
      'video_url' : download[2]
    })

  return jsonify({
    'count': len(statuses),
    'list': statuses
  })

@app.route('/status/<int:id>', methods=['GET'])
def status_by_id(id):

  if id < 0:
    abort(400)

  download_c  = store.query('SELECT * FROM downloads WHERE id = ?', (id,))
  download    = download_c.fetchone()

  if not download:
    abort(404)

  status  = {
    'video_url' : download[2],
    'status'    : download[3]
  }

  if status['status'] == 'READY':
    status['path']  = None

  return jsonify(status)
