from tortoise import fields, models
from datetime import datetime
from pydantic import BaseModel


class Device(models.Model):
    email       = fields.CharField(pk=True, max_length=255)
    user        = fields.CharField(max_length=100)
    nickname    = fields.CharField(max_length=100)
    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class DeviceCreateRequest(BaseModel):
    nickname: str
    email: str


class DeviceResponse(BaseModel):
    nickname: str
    email: str

    created_at: datetime
    updated_at: datetime