from datetime import datetime, timedelta
from typing import Dict, Any

import jwt

JWT_ALGORITHM = 'HS256'
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'  # dummy secret


def jwt_encode(data: Dict[str, Any], lifetime: timedelta | None = None) -> str:
    payload = data.copy()
    if lifetime:
        payload['exp'] = datetime.utcnow() + lifetime
    return jwt.encode(data=payload, key=SECRET_KEY, algorithm=JWT_ALGORITHM)


def jwt_decode(data: str) -> Dict[str, Any]:
    return jwt.decode(
        jwt=data,
        key=SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )
