import uvicorn
from fastapi import FastAPI

# import endpoints
from app.endpoints import UserEndpoint, RoleEndpoint

# import database models:
from app.db.session import engine
from app.db.base import DBBaseClass


def include_routes(app):
    # To include EndPoints:
    app.include_router(UserEndpoint.router)
    app.include_router(RoleEndpoint.router)


def create_tables():
    # generate automatically tables in database
    # the corresponding tables must be imported in app.db.base.py
    DBBaseClass.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI()
    include_routes(app)
    create_tables()
    return app


if __name__ == "__main__":
    api = start_application()
    uvicorn.run(api, host="0.0.0.0", port=8000)
