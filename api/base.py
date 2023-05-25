from fastapi import APIRouter

from api import route_login, route_music, route_users

api_router = APIRouter()


api_router.include_router(route_users.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
api_router.include_router(route_music.router, prefix="/music", tags=["music"])
