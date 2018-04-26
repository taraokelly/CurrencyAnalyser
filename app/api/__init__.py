""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   url_prefix='/api')

api_r = Api(api_bp)
api_rest = api_r.namespace('currencies', description='Currency data')

# OPTIONAL
@api_bp.after_request
def add_header(response):
    # Required for vue app served from localhost to access 127.0.0.1:5000
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

from app.api.rest import routing
