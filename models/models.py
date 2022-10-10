from datetime import datetime
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt
from fastapi import HTTPException

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
    
    gender = fields.BooleanField(default = None)
    age = fields.IntField(default = None)
    weight = fields.IntField(default = None)
    height = fields.IntField(default = None)
    goal = fields.CharField(100, default = None)
    experienceLevel = fields.CharField(100, default = None)
    
    @classmethod
    async def findUserByEmail(cls, email):
        return await cls.filter(email = email).first()
    @classmethod
    async def verify_email_signup(cls):
        '''
        send a message to the mail with a verification link
        '''
        pass
        
    #V2 add the hash thing
    async def verify_password_login(self, x):
        if self.password == x:
            return True
        return False
        
    @classmethod
    async def validate(cls, fields, data):
        for f in fields:
            if f == 'username':
                pass
                # the username is not used
            if f == 'email':
                pass
                # must have an @
            if f == 'password':
                pass
                # the big password validation method from geeksforgeeks
    async def setGender(self, data):
        self.gender = data
        self.save(update_fields = 'gender')
    async def setAge(self, data):
        self.age = data
        self.save(update_fields = 'age')
    async def setWeight(self, data):
        self.weight = data
        self.save(update_fields = 'weight')
    async def setHeight(self, data):
        self.height = data
        self.save(update_fields = 'height')
    async def setGoal(self, data):
        self.goal = data
        self.save(update_fields = 'goal')
    async def setExprienceLevel(self, data):
        self.experienceLevel = data
        self.save(update_fields = 'experienceLevel')
        
class Expert(User):
    pass
class Trainer(User):
    pass
