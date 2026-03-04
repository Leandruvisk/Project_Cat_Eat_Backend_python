#user_router
from sanic import Request, response, Blueprint
from src.models.user import UserCreateRequest, UserLoginRequest
from src.controler import UserController


user_routes = Blueprint('users', url_prefix='/user')
    

@user_routes.post('/create_user')
async def store(request: Request):
    user_request = UserCreateRequest(**request.json)
    user_response = await UserController.store(user_request)

    return response.json(user_response.model_dump(mode='json'), status=201)


@user_routes.post('/login')
async def login(request: Request):
    user_request = UserLoginRequest(**request.json)
    user_response = await UserController.login(user_request)

    return response.json(user_response.model_dump(mode='json'), status=201)