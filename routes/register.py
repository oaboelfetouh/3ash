from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException
from models.models import User , Expert, Trainer
from models.schemas import Email, Login, RegistrationIn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = await user.get()
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    return user

JWT_SECRET = 'MyNameIsOmarMohamedAboelfetouh&IDoArt'

router = APIRouter()

@router.post('/login')
async def login(login_pydantic : Login):
    model = User
    try:
        reg_dict = login_pydantic.dict(exclude_unset = False)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
        
    user = await model.findUserByEmail(reg_dict.email)
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Email is not signed up!')
    
    #V2 add the hash thing
    v = await user.verify_password_login(reg_dict.Password)
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Password is not correct')
    
    token = jwt.encode(reg_dict, JWT_SECRET)
    return {'access_token' : token, 'token_type' : 'bearer'}
    
    
@router.post('/register')
async def register(reg_pydantic : RegistrationIn):
    verify = reg_pydantic.verifyEmailAndUsername()
    if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='email or username is already used')
    
    verify = reg_pydantic.verify_password_length()
    if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Password is too short')
    
    verify = reg_pydantic.verify_password_again()
    if not verify : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Passwords dont match')
     
    try:
        reg_dict = reg_pydantic.dict(exclude_unset = False)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    #V2 add the hash thing
    userobj = await User.create(**reg_dict)
    await userobj.save()
    return userobj

@router.post('/register/genderin')
async def genderin(genderin : str, user = Depends(get_current_user)):
    user.setGender(genderin)
    return "done"
    
@router.post('/register/agein')
async def agein(agein : str, user = Depends(get_current_user)):
    user.setAge(agein)
    return "done"
    
@router.post('/register/w_heightin')
async def weightandhightin(weightin : float, heightin : float, user = Depends(get_current_user)):
    user.setHeight(heightin)
    user.setWeight(weightin)
    return "done"
    
@router.post('/register/goalin')
async def goalin(goalin : str, user = Depends(get_current_user)):
    user.setGoal(goalin)
    return "done"

@router.post('/register/experiencein')
async def experiencein(experiencein : str, user = Depends(get_current_user)):
    user.setExprienceLevel(experiencein)
    return "done"
    

@router.post('/forgetypassword')
async def forget_password():
    '''
    enter your mail - validate the mail - create a code of reset and save in the data base  - send a message with the link to reset :))
    '''
    pass
    

@router.post('/resetpassword/{code}')
async def reset_password(code:str):
    '''
    check if the code is correcrt as saved in the database
    check if the code isnot expired
    change the password!
    '''
    pass
