#!/usr/bin/python3
"""index module"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def myssatus():
    """sends json status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def count_objects():
    """retrieves the number of each object by type"""
    return jsonify({'amenities': storage.count('Amenity'),
                    'cities': storage.count('City'),
                    'places': storage.count('Place'),
                    'reviews': storage.count('Review'),
                    'states': storage.count('State'),
                    'users': storage.count('User')})
