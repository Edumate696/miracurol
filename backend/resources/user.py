from fastapi import APIRouter, Query

user_router = APIRouter(prefix='/api/v1/users', tags=['users'])


@user_router.get('/')
async def list_all_users(admin: bool = False):
    pass
