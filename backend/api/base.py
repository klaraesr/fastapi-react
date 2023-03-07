from fastapi import APIRouter

#from api.v1 import general
from api.v1 import users


api_router = APIRouter()
#api_router.include_router(general.router,prefix="",tags=["general"])
api_router.include_router(users.router,prefix="/users",tags=["users"])