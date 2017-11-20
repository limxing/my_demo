from apps.core import ma
from .models import *
from marshmallow import fields
class UserSchema(ma.ModelSchema):
    class Meta:
        model = User