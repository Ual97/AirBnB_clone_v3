#!/usr/bin/python3
"""index module"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route('/states/<ide>/cities', methods=['GET'], strict_slashes=False)
def view_cities(ide):
    """sends a list of all cities in a given state id"""
    objdct = storage.get("State", ide)
    if objdct is None:
        abort(404)
    cities = [c.to_dict() for c in objdct.cities]
    return jsonify(cities), 200


@app_views.route('/cities/<ide>', methods=['DELTE'])
def delete_city(ide):
    """deletes a city with a given id"""
    if request.method == 'DELETE':
        obj = storage.all(City, ide)
        if not obj:
            abort(404)
        storage.delete(obj)
        storage.save()
        return jsonify({})


@app_views.route('/cities/<ide>', methods=['GET'])
def get_city(ide):
    """gets a city by given id"""
    if request.method == 'GET':
        obj = storage.all(City, ide)
        if obj:
            return jsonify(obj.to_dict)
        abort(404)


@app_views.route('/states/<ide>/cities', methods=['POST'])
def post_city(ide):
    """posts a city with a given id"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    elif "name" not in request.get_json():
        abort(400, 'Missing name')
    else:
        obj_data = request.get_json()
        state = storage.get("State", ide)
        if state is None:
            abort(404)
        obj_data['state_id'] = state.id
        obj = City(**obj_data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<ide>', methods=['PUT'])
def put_city(ide):
    """puts a new city with given id"""
    robj = request.get_json()
    obj = storage.get(City, ide)
    if not obj:
        abort(404)
    if not robj:
        abort(400, 'Not a JSON')
    list = ["id", "created_at", "updated_at", "state_id"]
    for key, value in robj.items():
        if key not in list:
            setattr(obj, key, value)
    return obj.to_dict(), 201
