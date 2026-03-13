from src.models.user import User, UserCreateRequest, UserResponse, UserLoginRequest, UserHashResponse
import bcrypt
import argon2

class UserController:
    @staticmethod
    async def store(user_request: UserCreateRequest) -> UserResponse:
        user_create = await User.create(
            name=user_request.name,
            email=user_request.email,
            password=   user_request.password,
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
        
        user = await User.get(email=user_request.email)

        print(user.__dict__)
        password_bytes = user_request.password.encode("utf-8")
        stored_hash = user.password.encode("utf-8")
        
        ph = argon2.PasswordHasher()

        try:
            ph.verify(stored_hash, password_bytes)
        except Exception:
            raise Exception("Senha incorreta")
        
        # if not bcrypt.checkpw(password_bytes, stored_hash):
        #     raise Exception("Senha incorreta")

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
    
    @staticmethod
    async def delete(user_request: UserLoginRequest):
        print(user_request.__dict__)

        deleted_count = await User.filter(email=user_request.email).delete()

        return {"deleted": deleted_count}