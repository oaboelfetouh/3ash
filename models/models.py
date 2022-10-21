from datetime import datetime
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt
from fastapi import HTTPException, status

class User(Model):
    id = fields.IntField(pk=True)
    last_login = fields.DatetimeField(description="Last Login", default=None,null=True)
    picture = fields.CharField(max_length=200, default="",null=True)
    
    username = fields.CharField(50, unique=True)
    password = fields.CharField(128)
    
    email = fields.CharField(200, unique=True)
    email_verified = fields.BooleanField(default=False)
    
    is_blocked = fields.BooleanField(default = False)
    rank = fields.IntField(default = 1)
    
    gender = fields.BooleanField(default = False)
    age = fields.IntField(default = 0)
    weight = fields.IntField(default = 0)
    height = fields.IntField(default = 0)
    goal = fields.CharField(100, default = "")
    experienceLevel = fields.CharField(100, default = "")
    # YOU HAVE TO FIX THIS!!
    # CODE AND DATE HAS TO BE NONE
    forgot_password_code = fields.CharField(100, default = "")
    reset_code_issue_date = fields.DatetimeField(defualt = datetime.now(), null = True)
    forgot_password_attempts = fields.IntField(default=0)
    
    async def setForgotPasswordKey(self, SentCode):
        self.forgot_password_code = SentCode
        self.reset_code_issue_date = datetime.now()
        self.forgot_password_attempts += 1
        await self.save(update_fields=['forgot_password_code', 'reset_code_issue_date', 'forgot_password_attempts'])
        return self.forgot_password_code
        
    @classmethod
    async def findForgotPasswordKey(cls,SentCode):
        return await cls.filter(forgot_password_code=SentCode).first()
        
    async def getForgotPasswordKey(self):
        '''
        this function is used to return the body, request fields used for validation
        '''
        code_dict = {'forgot_password_code': self.forgot_password_code, 'reset_code_issue_date': self.reset_code_issue_date, 'forgot_password_attempts' : self.forgot_password_attempts}
        return code_dict , code_dict.keys()
        
    @classmethod
    async def validateForgotPasswordKey(cls, fieldNames, data):
           EXPIRATION_PERIOD_MINUTES = 30
           for f in fieldNames:
               if f == 'issue_date':
                   if data[f] + datetime.timedelta(minutes = EXPIRATION_PERIOD_MINUTES) < datetime.datetime.now():
                       return cls.getLabel(f) + " is expired"
                       
    async def resetPassword(self, new_password):
        #hashedPassword = pwd_context.hash(new_password)
        #self.password = hashedPassword
        self.password = new_password
        await self.save(update_fields=["password"])
        
    async def hasPicture(self):
        if self.picture != "" : return True
        return False
        
    @classmethod
    async def verifyEmailAndUsername(cls, data, sent_fields):
        for f in sent_fields:
            if f == 'email':
                x = await cls.filter(email = data[f]).first()
                if x is not None :  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='this email is taken, forgot your password?')
                if '@' not in data[f]:  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='this email is not valid')
                if len(data[f]) < 5 :  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='this email is not valid')
            if f == 'username':
                x = await cls.filter(username = data[f]).first()
                if x is not None :  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='this username is already taken')
            
            if f == 'password':
                if len(data[f]) < 8 : raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='password is too short')
                
            if data['password'] != data['Password_Again']: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='passwords dont match')
    @classmethod
    async def findUserById(cls, user_id):
        return await cls.filter(id = user_id)
    @classmethod
    async def findUserByEmail(cls, email):
        return await cls.filter(email = email).first()
    @classmethod
    async def findUserByUsername(cls, username):
        return await cls.filter(username = username).first()
    @classmethod
    async def verifyEmail(cls):
        '''
        send a message to the mail with a verification link
        '''
        pass
        
    #V2 add the hash thing
    async def verify_password_login(self, x):
        if self.password == x:
            return True
        return False
        
    async def setGender(self, data):
        self.gender = data
        await self.save(update_fields = ['gender'])
    async def setAge(self, data):
        self.age = data
        await self.save(update_fields = ['age'])
    async def setWeight(self, data):
        self.weight = data
        await self.save(update_fields = ['weight'])
    async def setHeight(self, data):
        self.height = data
        await self.save(update_fields = ['height'])
    async def setGoal(self, data):
        self.goal = data
        await self.save(update_fields = ['goal'])
    async def setExprienceLevel(self, data):
        self.experienceLevel = data
        await self.save(update_fields = ['experienceLevel'])
        
class Expert(User):
    pass
class Trainer(User):
    pass
