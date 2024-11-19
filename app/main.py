import uvicorn
from fastapi import FastAPI
from app.config.dbconfig import db
from dotenv import load_dotenv
import os
from app.model.posts import Post
from random import randrange


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the .env file")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def init_app():
    db.init()

    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version="1.0"
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    return app


app = init_app()


@app.get("/")
async def root():
    return {"message": "Welcomt to FastAPI"}


@app.get("/test/{item_id}/")
async def test(item_id: str):
    return {"Hello ": item_id}


my_posts = [{"id": 1, "title": "title of post 1", "content": "content of post 1"},
            {"id": 2, "title": "favorite foods", "content": "I like pizza"}]


@app.get("/getposts")
async def get_posts():
    return {"message": my_posts}


@app.post("/posts")
async def create_posts(payLoad: Post):
    post_dict = payLoad.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    print(payLoad.model_dump_json)
    return {"data": post_dict}


def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
