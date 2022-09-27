from datetime import datetime
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt
from fastapi import HTTPException

class User(Model):
    id = fields.IntField(pk=True)
    last_login = fields.DatetimeField(description="Last Login", default=datetime.datetime.now,null=True)
    picture = fields.CharField(max_length=200, default="",null=True)
    
    username = fields.CharField(50, unique=True)
    password = fields.CharField(128)
    
    email = fields.CharField(200, unique=True)
    email_verified = fields.BooleanField(default=False)
    
    is_blocked = fields.BooleanField(default = False)
    rank = fields.IntField(default = 1)
    
    gender = fields.CharField(default = None)
    age = fields.IntField(default = None)
    weight = fields.IntField(default = None)
    height = fields.IntField(default = None)
    goal = fields.CharField(default = None)
    experienceLevel = fields.CharField(default = None)
    
    def verify_email_signup(self):
        pass
    
    def verify_password_login(self, password):
        if self.password == password:
            return True
        return False


class Expert(user):
    Permitted = fields.BooleanField(default = True)
    NumOfArticle = fields.IntField()

class Trainer(user):
    Stars = fields.IntField(5)
    NumOfStudents = fields.IntField()

