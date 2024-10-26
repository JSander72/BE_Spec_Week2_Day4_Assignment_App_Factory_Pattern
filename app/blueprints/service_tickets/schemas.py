from marshmallow import Schema, fields, validate

class ServiceTicketSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    status = fields.Str(required=True, validate=validate.OneOf(["open", "in_progress", "closed"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)