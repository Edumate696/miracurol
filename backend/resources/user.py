from fastapi import APIRouter

from backend.models.user import UserSummary

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.get('/me', response_model=UserSummary)
async def get_current_user_summary():
    pass


@router.get('/{id}', response_model=UserSummary)
async def get_user_summary(id: int):
    pass
