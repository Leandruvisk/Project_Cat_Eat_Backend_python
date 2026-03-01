from sanic import Sanic
from sanic.response import text
from tortoise.contrib.sanic import register_tortoise
from src.routes import routes

app = Sanic(__name__)
app.blueprint(routes)

register_tortoise(
    app,
    db_url="postgres://comedor:123456@127.0.0.1:5432/comedor_gato",
    modules={"models": ["src.models.user"]},
    generate_schemas=True,
)

@app.get("/")
async def hello(request):
    return text("Hello World!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)