#!/usr/bin/python3
"""index module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """returns all amenitities objects"""
    objdct = storage.all(Amenity)
    lst = []
    # foreach object in the values of the object dictionary
    for obj in objdct.values():
        # transform it to a dictionary an add to list
        dct = obj.to_dict()
        lst.append(dct)
    return jsonify(lst)


@app_views.route('/amenities/<ide>',
                 methods=['GET'], strict_slashes=False)
def get_amenity_id(ide):
    """returns given amenity by id"""
    amenity = storage.get("Amenity", ide)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<ide>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(ide):
    """deletes amenity by id"""
    amenity = storage.get("Amenity", ide)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenities():
    """post new amenity"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    elif "name" not in request.get_json():
        abort(400, 'Missing name')
    else:
        robj = request.get_json()
        obj = Amenity(**robj)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/amenities/<ide>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(ide):
    '''
        update existing amenity object
    '''
    if not request.get_json():
        abort(400, 'Not a JSON')
    obj = storage.get("Amenity", ide)
    if obj is None:
        abort(404)
    robj = request.get_json()
    obj.name = robj['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
