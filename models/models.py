import os
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv
import uuid
import datetime

load_dotenv()

database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_host = os.getenv('DATABASE_HOST')

database_path = 'postgres://{}@{}/{}'.format(database_user, database_host, database_name)

db = SQLAlchemy()


"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()
    db.session.close()
    return db