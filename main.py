from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.base import api_router
from core.config import settings
from db.base_class import Base
from db.sessions import engine


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    create_tables()
    return app


app = start_application()
