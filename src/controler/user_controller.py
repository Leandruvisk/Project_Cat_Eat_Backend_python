from src.models.user import User, UserRequest, UserResponse

class UserController:
    @staticmethod
    async def store(user_request: UserRequest) -> UserResponse:
        user = await User.create(
            name=user_request.name,
            email=user_request.email,
            password=user_request.password,
        )

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )