#!/usr/bin/python3
"""index module"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states')
def view_states():
    """sends list of state objects as dicts"""
    objdct = storage.all(State)
    lst = []
    # foreach object in the values of the object dictionary
    for obj in objdct.values():
        # transform it to a dictionary an add to list
        dct = obj.to_dict()
        lst.append(dct)
    return jsonify(lst)


@app_views.route('/state/<ide>', methods=['GET', 'DELETE', 'POST', 'PUT'])
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

    elif request.method == 'POST':
        return "wop"
