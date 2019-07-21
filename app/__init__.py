from flask import Flask

from config import BaseConfig
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)

login = LoginManager(app)

migrate = Migrate(app,db)


from app import routes
from app.models import models
