#!/usr/bin/python3
"""index module"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import City

@app_views.route('/states/<ide>/cities', methods=['GET'])
def view_cities(ide):
    """sends a list of all cities in a given state id"""
    if (request.method == 'GET'):
        objdct = storage.all(City)
        lst = []
        for obj in objdct:
            if obj.state_id == ide:
                dct = obj.to_dict()
                lst.append(dct)
        return jsonify(lst)
