#!/usr/bin/python3
"""index module"""
from flask import jsonify
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


@app_views.route('/states/a')
def view_a_state():
    """aaaaaaaaaaaaaaaa"""
    return "a"
