from main import app, store
from flask import request, jsonify, abort

@app.route('/status', methods=['GET'])
def status_list():
  
  downloads_c  = store.query('SELECT * FROM downloads')
  statuses  = []

  for download in downloads_c:
    statuses.append({
      'id'        : download[0],
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

  return jsonify(status)


@app.route('/logs', methods=['GET'])
def logs_list():
  
  logs_c  = store.query('SELECT * FROM logs')
  logs  = []

  for log in logs_c:
    logs.append({
      'id'        : log[0],
      'date'      : log[1],
      'level'     : log[2],
      'message' : log[3]
    })

  return jsonify({
    'count': len(logs),
    'list': logs
  })

@app.route('/logs/<level>', methods=['GET'])
def logs_list_by_level(level):

  if not level or not isinstance(level, str):
    abort(400)
  
  logs_c  = store.query('SELECT * FROM logs WHERE level = ?', (level,))
  logs  = []

  for log in logs_c:
    logs.append({
      'id'        : log[0],
      'date'      : log[1],
      'level'     : log[2],
      'message'   : log[3]
    })

  return jsonify({
    'count': len(logs),
    'list': logs
  })


@app.route('/logs/<int:id>', methods=['GET'])
def log_by_id(id):

  if id < 0:
    abort(400)

  log_c  = store.query('SELECT * FROM logs WHERE id = ?', (id,))
  log    = log_c.fetchone()

  if not log:
    abort(404)

  log  = {
      'date'      : log[1],
      'level'     : log[2],
      'message'   : log[3]
  }

  return jsonify(log)
