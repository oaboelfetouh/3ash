import datetime
import uuid

from jose import JWTError, jwt
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException, Request
from models.models import User , Expert, Trainer
from models.schemas import Email, Login, RegistrationIn,NewPassword
from fastapi.security import OAuth2PasswordBearer
from dependencies import get_user, JWT_SECRET
try :
    from dependencies import JWT_SECRET
except:
    JWT_SECRET = "IamOmarAboelfetouhMahmoudAndIDoART01129461404"

router = APIRouter()

@router.post('/login')
async def login(login_pydantic : Login):
    model = User
    try:
        reg_dict = login_pydantic.dict(exclude_unset = False)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
        
    user = await model.findUserByEmail(reg_dict["email"])
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Email is not signed up!')
    
    #V2 add the hash thing
    v = await user.verify_password_login(reg_dict["password"])
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Password is not correct')
    
    # the token generation
    token = jwt.encode({"user_id": user.id}, JWT_SECRET, algorithm="HS256")
    ret = {
        "user": {
            "username": user.username,
            "avatar": user.picture if user.hasPicture() else None,
        },
        "token": token
    }
    return ret

    
# works and tested
@router.post('/register')
async def register(reg_pydantic : RegistrationIn):
    model = User
    try:
           reg_dict = reg_pydantic.dict(exclude_unset = False)
    except:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    # verify the input
    verify = await User.verifyEmailAndUsername(reg_dict, reg_dict.keys())
    if verify is not None:
        return await verify
    
    # save in database
    user = await model.create(**reg_dict)
    await user.save()
    # the token generation
    token = jwt.encode({"user_id": user.id}, JWT_SECRET, algorithm="HS256")
    ret = {
        "user": {
            "username": user.username,
            "avatar": user.picture if user.hasPicture() else None,
        },
        "token": token
    }
    return ret

@router.post('/register/genderin')
async def genderin(genderin : bool,
user = Depends(get_user)
):
    await user.setGender(genderin)
    return "done"
    
@router.post('/register/agein')
async def agein(agein : int,
user = Depends(get_user)
):
    await user.setAge(agein)
    return "done"
    
@router.post('/register/w_heightin')
async def weightandhightin(weightin : int, heightin : int,
user = Depends(get_user)
):
    await user.setHeight(heightin)
    await user.setWeight(weightin)
    return "done"
    
@router.post('/register/goalin')
async def goalin(goalin : str,
user = Depends(get_user)
):
    await user.setGoal(goalin)
    return "done"

@router.post('/register/experiencein')
async def experiencein(experiencein : str
, user = Depends(get_user)
):
    await user.setExprienceLevel(experiencein)
    return "done"
    

def Generate_code():
    '''
    this function should generate a unique string everythime it runs
    '''
    code = uuid.uuid1()
    return code
    
    
@router.post('/forgotpassword')
async def forgot_password(req: Request, email:Email):
    # check user exsited
    model = User
    user = await model.findUserByEmail(email.dict().get("email"))
    if not user:
        raise HTTPException(HTTP_404_NOT_FOUND, "Not Found")
    
    # create a reset code and save it in the db
    code = Generate_code()
    r = await user.setForgotPasswordKey(code)
    '''
    send the mail with the link containg r : /forgot-password/{code}
    '''
    return {"your reset code is : " : r }

#add user id and add it to the database search
@router.post('/forgot-password/{code}')
async def reset_password(code:str, new_password: NewPassword):
    # reset the password in the database
    
    # check code exsits
    model = Buser
    user = await model.findForgotPasswordKey(code)
    if not user:
        raise HTTPException(HTTP_404_NOT_FOUND, "Code is Incorrect")
    
    # validate if expired
    body, resource_fields = await user.getForgotPasswordKey()
    v = await model.validateForgotPasswordKey(resource_fields,body)
    if v is not None:
        return v
    
    # validate the password
    body, resource_fields = await new_password.getData()
    v = await rest_logic.validate(model, resource_fields, body)
    if v is not None:
        return v
    # reset the password in the database
    r = await user.resetPassword(body["password"])
    return "Done"



@router.get('/test_deletethis')
async def get_all_users():
    return await User.all()
