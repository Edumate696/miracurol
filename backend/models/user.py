from datetime import datetime

from pydantic import EmailStr

from backend.models.base import Base


class User(Base):
    is_admin: bool = False


class UserSummary(User):
    email: EmailStr = None
    phone: str = None
    address: str = None
    created_at: datetime
    updated_at: datetime
