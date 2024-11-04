from db import db


class ItemModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationshiop(
        "ItemModel", back_populates="store", lazy="dynamic"
    )  # This line is used to create a relationship between the StoreModel and the ItemModel
