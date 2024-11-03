from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)      # The ID field is read-only
    name = fields.Str(required=True)     # The name field is required
    price = fields.Float(required=True)  # The price field is required
    store_id = fields.Str(required=True) # The store_id field is required

class ItemListSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
