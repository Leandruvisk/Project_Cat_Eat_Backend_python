from src.models.user import User, UserCreateRequest, UserResponse, UserLoginRequest

class UserController:
    @staticmethod
    async def store(user_request: UserCreateRequest) -> UserResponse:
        user_create = await User.create(
            name=user_request.name,
            email=user_request.email,
            password=user_request.password,
        )

        return UserResponse(
            id=user_create.id,
            name=user_create.name,
            email=user_create.email,
            created_at=user_create.created_at,
            updated_at=user_create.updated_at,
        )

    @staticmethod
    async def login(user_request: UserLoginRequest) -> UserResponse:
        
        user_login = await User.get(
            email=user_request.email,
            password=user_request.password,
        )
    
        return UserResponse(
            id=user_login.id,
            name=user_login.name,
            email=user_login.email,
            created_at=user_login.created_at,
            updated_at=user_login.updated_at,
        )