#!/usr/bin/python3
"""index module"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """returns all users"""
    objdct = storage.all(User)
    lst = []
    for obj in objdct.values():
        dct = obj.to_dict()
        lst.append(dct)
    return jsonify(lst)


@app_views.route('/users/<ide>', methods=['GET'], strict_slashes=False)
def get_user_id(ide):
    """returns a user by id"""
    user = storage.get("User", ide)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<ide>', methods=['DELETE'], strict_slashes=False)
def delete_user(ide):
    """deletes user by given id"""
    user = storage.get("User", ide)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Posts new User"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    elif "email" not in request.get_json():
        abort(400, 'Missing email')
    elif "password" not in request.get_json():
        abort(400, 'Missing password')
    else:
        robj = request.get_json()
        obj = User(**robj)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/users/<ide>', methods=['PUT'], strict_slashes=False)
def update_user(ide):
    '''
        update existing user object
    '''
    if not request.get_json():
        abort(400, 'Not a JSON')
    obj = storage.get("User", ide)
    if obj is None:
        abort(404)
    robj = request.get_json()
    list = ("id", "email", "created_at", "updated_at")
    for i in robj.keys():
        if i in list:
            pass
        else:
            setattr(obj, i, robj[i])
    obj.save()
    return jsonify(obj.to_dict()), 200
