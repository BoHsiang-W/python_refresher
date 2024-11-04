from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)  # The ID field is read-only
    name = fields.Str(required=True)  # The name field is required
    price = fields.Float(required=True)  # The price field is required

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlainStoreSchema):
    sotre_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(lambda: StoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(lambda: ItemSchema()), dump_only=True)  # The items field is a list of PlainItemSchema objects
