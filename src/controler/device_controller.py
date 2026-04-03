from src.models.devices import Device, DeviceCreateRequest, DeviceResponse

class DeviceController:
   
    @staticmethod
    async def device_create(device_request: DeviceCreateRequest) -> DeviceResponse:
        device_create = await Device.create(
            name=device_request.nickname,
            email=device_request.email,
        )

        return DeviceResponse(
            name=device_create.nickname,
            email=device_create.email,
            created_at=device_create.created_at,
            updated_at=device_create.updated_at,
        )