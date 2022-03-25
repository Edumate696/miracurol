from fastapi.security.oauth2 import OAuth2PasswordBearer
from passlib.context import CryptContext


class SecurityBase:
    _oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl='api/o/oauth2/token',
        description='Oauth 2.0 password authentication',
    )
    _pwd_context = CryptContext(
        schemes=['bcrypt'],
        deprecated='auto',
    )
