from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base


class EntityBase(declarative_base()):
    """Base Entity class for all entities"""
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'extend_existing': True
    }


class EntityUser(EntityBase):
    """Represents all the users in the entire application"""
    __tablename__ = 'user'

    # Columns
    id: int = Column('id', Integer, primary_key=True)
    name: str = Column('name', String)
    email: str | None = Column('email', String)
    phone: str | None = Column('phone', String)
    address: str | None = Column('address', String)
    password: str = Column('password', String)
    is_admin: bool = Column('is_admin', Boolean)
    created_at: datetime = Column('created_at', DateTime)
    updated_at: datetime = Column('updated_at', DateTime)
    last_known_loc: str | None = Column('last_known_loc', String)


class EntityDoctor(EntityBase):
    """Represents all the doctors in the entire application"""
    __tablename__ = 'doctor'

    # Columns
    id: int = Column('id', Integer, primary_key=True)
    root_id: int = Column('root_id', Integer)
    professional_statement: str = Column('professional_statement', String)
    practicing_from: datetime = Column('practicing_from', DateTime)
