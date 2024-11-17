import uvicorn
from fastapi import FastAPI
from app.config.dbconfig import db


def init_app():
    db.init()

    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version=1
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
def read_root():
    return {"message": "Hello, World!"}


def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
