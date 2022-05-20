#!/usr/bin/python3
"""app module"""
from os import environ
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardwn(exception):
    storage.close()

@app.route('/hello')
def hello():
     return 'Hello, World!'

if __name__ == '__main__':
    app.run(host=environ['HBNB_API_HOST'],
            port=environ['HBNB_API_PORT'],
            debug=True, threaded=True)
