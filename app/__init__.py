

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localdb.sql'

db = SQLAlchemy(app)

migrate = Migrate(app,db)


from app.crud import routes
from app.crud import models




