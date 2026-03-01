#modelo de cada tabela

from tortoise import fields, models
from datetime import datetime
from pydantic import BaseModel


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100) #dps usar uma hash

    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class UserRequest(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    created_at: datetime
    updated_at: datetime
