from app import db
from .operations import Operations


class BaseModel(db.Model,Operations):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
 