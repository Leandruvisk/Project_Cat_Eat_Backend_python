from sanic import Blueprint
from .user_router import user_routes

routes = Blueprint.group(user_routes)