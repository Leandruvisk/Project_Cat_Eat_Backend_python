#user_router
from sanic import Request, response, Blueprint
from src.models.user import UserCreateRequest, UserLoginRequest
from src.controler import UserController
import bcrypt
from argon2 import PasswordHasher


user_routes = Blueprint('users', url_prefix='/user')
    

@user_routes.post('/create_user')
async def store(request: Request):

    user_request = UserCreateRequest(**request.json)

    ph = PasswordHasher()
    user_request.password = ph.hash(user_request.password)

    user_response = await UserController.store(user_request)

    return response.json(user_response.model_dump(mode='json'), status=201)

@user_routes.post('/login')
async def login(request: Request):

    user_request = UserLoginRequest(**request.json)

    try:
        user_response = await UserController.login(user_request)
        return response.json(user_response.model_dump(mode='json'), status=200)

    except Exception as e:
        return response.json({"error": str(e)}, status=401)
    

@user_routes.post('/delete')
async def delete_user(request: Request):
    
    user_request = UserLoginRequest(**request.json)

    try:
        user_response = await UserController.login(user_request)
        user_data = user_response.model_dump(mode='json')
        user_response = await UserController.delete(user_response)
        return response.json(user_data, status=200)

        
    except Exception as e:
        print('deu ruim')
        return response.json({"error": str(e)}, status=400)