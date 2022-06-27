from passlib import pwd
from passlib.context import CryptContext

_pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def generate() -> str:
    return pwd.genword()


def hash(plain_password: str) -> str:
    return _pwd_context.hash(plain_password)


def verify_and_update(plain_password: str, hashed_password: str) -> (bool, str | None):
    return _pwd_context.verify_and_update(plain_password, hashed_password)
