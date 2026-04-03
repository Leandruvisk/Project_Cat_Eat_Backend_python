import os
from sanic import Sanic
from sanic.response import text
from tortoise.contrib.sanic import register_tortoise
from src.routes import routes

app = Sanic(__name__)
app.blueprint(routes)

db_url = os.getenv("DB_URL")

# print("🔥 DB_URL:", db_url)  # DEBUG

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["src.models.user"]},
    generate_schemas=True,
)

@app.get("/")
async def hello(request):
    return text("Hello World!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)