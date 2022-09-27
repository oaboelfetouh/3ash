from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query

JWT_SECRET = 'MyNameIsOmarMohamedAboelfetouh&IDoArt'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post('/login')
async def login(login_pydantic : Login):
    try:
        reg_dict = login_pydantic.dict(exclude_unset = False)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    u = verify_user(reg_dict.email, reg_dict.password)
    if not u: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Email or Password is not correct')
    token = jwt.encode(reg_dict, JWT_SECRET)
    return {'access_token' : token, 'token_type' : 'bearer'}
    
    
@router.post('/register')
async def register(reg_pydantic : RegistrationIn):
    veridy = reg_pydantic.verifyEmailAndUsername()
     if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='email or username is already used')
    
    verify = reg_pydantic.verify_password_length()
    if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Password is too short')
    
    verify = reg_pydantic.verify_password_again()
     if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Passwords dont match')
     
    try:
        reg_dict = reg_pydantic.dict(exclude_unset = False)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    
    userobj = await User.create(**reg_dict)
    await userobj.save()

@router.post('/forgetypassword')
async def forget_password():
    pass

@router.post('/genderin')
async def genderin(user = Depends(get_current_user), genderin : str):
    user.gender = genderin
    return "done"
    
@router.post('/agein')
async def agein(user = Depends(get_current_user), agein : str):
    user.age = agein
    return "done"
    
@router.post('/w_heightin')
async def weightandhightin(user = Depends(get_current_user), weightin : float, heightin : float):
    user.height = heightin
    user.weight = weightin
    return "done"
    
@router.post('/goalin')
async def goalin(user = Depends(get_current_user), goalin : str):
    user.goal = goalin
    return "done"

@router.post('/experiencein')
async def experiencein(user = Depends(get_current_user), experiencein : str):
    user.experience = experiencein
    return "done"
    
