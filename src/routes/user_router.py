#user_router
from sanic import Request, response, Blueprint
from src.models.user import UserRequest
from src.controler import UserController


user_routes = Blueprint('users', url_prefix='/user')
    

@user_routes.post('/')
async def store(request: Request):
    user_request = UserRequest(**request.json)
    user_response = await UserController.store(user_request)

    return response.json(user_response.model_dump(mode='json'), status=201)
