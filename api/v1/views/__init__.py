from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import view_states, view_a_state
from api.v1.views.cities import view_cities, delete_city, get_city, post_city, put_city
