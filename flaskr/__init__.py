import os
import sys
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
)
import requests

from models.models import setup_db, db, Users, Countries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import sys

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    CORS(app)


    @app.route('/')
    def index():
        pass

    # Launch.

    # Default port:
    if __name__ == '__main__':
        app.run(debug=True)


    return app
