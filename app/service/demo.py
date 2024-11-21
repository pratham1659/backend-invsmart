# import uvicorn
# from fastapi import FastAPI
# from app.config.dbconfig import db
# from fastapi.params import Body
# from pydantic import BaseModel
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from dotenv import load_dotenv
# import os
# from app.model.posts import Post


# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY")
# if not SECRET_KEY:
#     raise ValueError("SECRET_KEY is not set in the .env file")

# ALGORITHM = "HS256"

# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# def init_app():
#     db.init()

#     app = FastAPI(
#         title="Inventory Insight App",
#         description="Login Page",
#         version="1.0"
#     )

#     @app.on_event("startup")
#     async def startup():
#         await db.create_all()

#     @app.on_event("shutdown")
#     async def shutdown():
#         await db.close()

#     return app


# app = init_app()


# @app.get("/")
# async def root():
#     return {"message": "Welcomt to FastAPI"}


# @app.get("/test/{item_id}/")
# async def test(item_id: str):
#     return {"Hello ": item_id}


# @app.post("/selectfilter")
# async def selectfilter(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"message": f"title {payLoad['title']} content: {payLoad['content']}"}


# @app.post("/selectfilter")
# async def selectfilter(payLoad: Post):
#     print(payLoad.model_dump)
#     print(f"Title: {payLoad.title}")
#     print(f"Description: {payLoad.content}")
#     print(f"Published: {payLoad.published}")
#     print(f"Ratings: {payLoad.rating}")
#     return {"message": payLoad}


# @app.get("/posts/latest")
# async def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"message": post}


# @app.get("/posts/{id}")
# async def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": f"post with id: {id} was not found"}
#     return {"post_details": post}


# def start():
#     """Launched with 'poetry run start' at root level """
#     uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
