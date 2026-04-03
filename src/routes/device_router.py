from sanic import Request, response, Blueprint
from src.models.devices import Device, DeviceCreateRequest, DeviceResponse
from src.controler import DeviceController


device_routes = Blueprint('devices', url_prefix='/devices')

@device_routes.post('/create_device')
async def device_store(device_request: DeviceCreateRequest) -> DeviceResponse:
    device_create = await Device.create(
        name=device_request.nickname,
        email=device_request.email,
    )

    return DeviceResponse(
        user=device_create.user,
        name=device_create.nickname,
        email=device_create.email,
        created_at=device_create.created_at,
        updated_at=device_create.updated_at,
    )
