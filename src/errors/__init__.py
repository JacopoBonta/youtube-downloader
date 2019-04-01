from main import app
from flask import make_response, jsonify

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def invalid_parameters(error):
    return make_response(jsonify({'error': 'Invalid parameter'}), 400)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal server error'}), 500)