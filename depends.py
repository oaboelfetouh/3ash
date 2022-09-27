#imports

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = await user.get()
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    return user

async def verify_user(email: str, password: str):
    user__ = await user.get(email=email)
    if not user:
        return False
    if not user__.verify_password_login(password):
        return False
    return user__
