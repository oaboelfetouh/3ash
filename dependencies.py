from jose import JWTError, jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Depends, HTTPException, Path, Query, Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from models.models import User
auth_schema = HTTPBearer()
JWT_SECRET = "IamOmarAboelfetouhMahmoudAndIDoART01129461404"

async def jwt_required(
    request: Request, token: HTTPAuthorizationCredentials = Depends(auth_schema)
):
    credentials_exception = HTTPException(HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token.credentials, JWT_SECRET)
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    request.scope["user_id"] = user_id
    return user_id


async def get_user(user_id=Depends(jwt_required)):
    user = await User.findUserById(user_id=user_id)
    if not user:
        raise HTTPException(HTTP_404_NOT_FOUND)
    return user[0]
