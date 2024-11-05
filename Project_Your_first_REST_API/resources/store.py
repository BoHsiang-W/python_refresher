import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from schemas import StoreSchema
from models import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Store", __name__, description="Store operations")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        item = StoreModel.query.get_or_404(store_id)
        return item

    def delete(self, store_id):
        item = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("Deleting a store is not implemented yet")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A Store with the same name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the store.")
