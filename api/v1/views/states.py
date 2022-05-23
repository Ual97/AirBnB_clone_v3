#!/usr/bin/python3
"""index module"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def view_states():
    """sends list of state objects as dicts"""
    if (request.method == 'GET'):
        objdct = storage.all(State)
        lst = []
        # foreach object in the values of the object dictionary
        for obj in objdct.values():
            # transform it to a dictionary an add to list
            dct = obj.to_dict()
            lst.append(dct)
        return jsonify(lst)
    elif (request.method == 'POST'):
        robj = request.get_json()
        if not robj:
            abort(400, 'Not a JSON')
        elif "name" not in robj:
            abort(400, "Missing name")
        else:
            obj = State(**robj)
            storage.new(obj)
            storage.save()
            return obj.to_dict(), 201


@app_views.route('/states/<ide>', methods=['GET', 'DELETE', 'PUT'])
def view_a_state(ide):
    """operations on state object by id"""
    if request.method == 'GET':
        obj = storage.get(State, ide)
        if obj:
            return jsonify(obj.to_dict())
        abort(404)

    elif request.method == 'DELETE':
        obj = storage.get(State, ide)
        if not obj:
            abort(404)
        storage.delete(obj)
        storage.save()
        return jsonify({})
