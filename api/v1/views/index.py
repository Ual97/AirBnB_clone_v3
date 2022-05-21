#!/usr/bin/python3
"""index module"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def myssatus():
    """sends json status"""
    return jsonify({'status': 'OK'})
