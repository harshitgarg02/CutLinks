import os
from flask import *
from flask_sqlalchemy import *
from sqlalchemy.sql import *
from config import *
from slugify import slugify
from os import environ
from flask_restful import *
from flask_restful import reqparse
import random
import re

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or ('sqlite:///' + os.path.join(os.path.join(basedir, 'database'),'databse.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

errors = {
    'MethodNotAllowed': {
        'status': 405,
        'message': 'Method Not Allowed! Please use Post API Call for Shortening URL and Get API Call for Fetching URL Information.'
    }
}

api = Api(app, prefix="/api", errors=errors)

db = SQLAlchemy(app)

from app.functions import *
from app import db_table
from app.db_table import *
from app import login,register,dashboard,logout
from app import home,urls,help
from app import api
from app.api import *

create_admin()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
