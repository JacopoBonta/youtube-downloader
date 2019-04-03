from main import app
from flask import request, jsonify, abort

@app.route('/status', methods=['GET'])
def status_list():
  return jsonify({
    'count': 0,
    'list': []
  })

@app.route('/status/<int:id>', methods=['GET'])
def status_by_id(id):
  return jsonify({
    'id': id
  })
