"""Module contains schemas for validating json objects received in request"""

from marshmallow import fields as f, Schema, validate


class ClientItemSchema(Schema):
    id = f.String(required=True)
    is_active = f.Boolean(data_key='isActive', truthy={True}, falsy={False})
    age = f.Integer(strict=True)
    name = f.String()
    gender = f.String(validate=validate.OneOf(["male", "female"]))
    company = f.String()
    email = f.Email(required=True)
    phone = f.String()
    address = f.String()


class ClientsListSchema(Schema):
    clients = f.List(f.Nested(ClientItemSchema), required=True, validate=validate.Length(min=1))
