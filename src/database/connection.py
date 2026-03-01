#inicializa conexão com o postgresql via tortoise
from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="postgres://comedor:123456@127.0.0.1:5432/comedor_gato",
        modules={"models": ["src.models.user"]}
    )
    await Tortoise.generate_schemas()