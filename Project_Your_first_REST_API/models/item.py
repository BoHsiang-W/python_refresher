from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True),                 # primary_key=True means that the id is the primary key
    name = db.Column(db.String(80), unique=True, nullable=False)  # unique=True means that the name has to be unique, nullable=False means that the name cannot be empty
    price = db.Column(db.Float(precision=2))                      # precision=2 means that the price will have 2 decimal places
    store_id = db.Column(db.Integer, unique=True, nullable=False) # unique=True means that the store_id has to be unique, nullable=False means that the store_id cannot be empty