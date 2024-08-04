#!/usr/bin/python3
"""Start api"""


from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/app/v1')


from api.v1.views.index import *
