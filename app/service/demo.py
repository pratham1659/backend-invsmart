import uvicorn
from fastapi import FastAPI
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi. security import Auth2PasswordBearer, Auth2PasswordRequestForm
from app.config.dbconfig import db


def init_app():
    # db.init()

    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version="1.0"
    )

    # @app.on_event("startup")
    # async def startup():
    #     await db.create_all()

    # @app.on_event("shutdown")
    # async def shutdown():
    #     await db.close()

    return app


app = init_app()


@app.get("/test/{item_id}/")
async def test(item_id: str):
    return {"Hello ": item_id}


def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)