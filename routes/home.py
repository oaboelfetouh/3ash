from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException
from models.models import User , Expert, Trainer
from models.schemas import Email, Login, RegistrationIn
from dependencies import get_user, JWT_SECRET

router = APIRouter()

async def load_cach():
    '''
    loads the latest posts and stories in a cach memory :))
    it returns the stories and posts based on the user's follosing list
    DB NOTE: you will create a model for the the posts and stories :))
    '''
    pass
# stories, posts = load_cach()
@router.get('/home')
async def stories(user = Depends(get_user)):
    '''
    returns a list of stories based on the user's following list :)
    DB NOTE: add a user following and followers lists :)
    '''
    pass
    
# how to add 2 functions to the same endpoint?
# or should i simply merge them ?
@router.get('/home')
async def posts(user = Depends(get_user)):
    '''
    returns a list of posts based on the user following lists :))
    '''
    pass

'''
learn how to post likes and comments


'''
