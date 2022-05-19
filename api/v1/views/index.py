#!/usr/bin/python3
from flask import jsonify
import app_views from api.v1.views


@app.route('/status')
def hello():
    return jsonify({'status': 'ok'})
