# import uvicorn
# from fastapi import FastAPI
# from app.config.dbconfig import db
# from pydantic import BaseModel
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from dotenv import load_dotenv
# import os


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


# class Data(BaseModel):
#     name: str


# @app.post("/create/")
# async def create(data: Data):
#     return {"data": data}


# @app.get("/test/{item_id}/")
# async def test(item_id: str):
#     return {"Hello ": item_id}


# # def start():
# #     """Launched with 'poetry run start' at root level """
# #     uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
