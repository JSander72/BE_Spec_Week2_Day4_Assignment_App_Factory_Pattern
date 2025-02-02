from marshmallow import Schema, fields

class MechanicSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)
    years_of_experience = fields.Int(required=True)

class CreateMechanicSchema(Schema):
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)
    years_of_experience = fields.Int(required=True)

class UpdateMechanicSchema(Schema):
    name = fields.Str()
    expertise = fields.Str()
    years_of_experience = fields.Int()