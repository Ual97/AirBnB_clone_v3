#!/usr/bin/python3
"""app module"""
from os import environ
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardwn(exception):
    storage.close()


if __name__ == '__main__':
    if 'HBNB_API_HOST' in environ:
        hst = '0.0.0.0'
    else:
        hst = environ['HBNB_API_HOST']
    if 'HBNB_API_PORT' in environ:
        prt = environ['HBNB_API_PORT']
    else:
        prt = '5000'
    app.run(host=hst, port=prt,
            debug=True, threaded=True)
