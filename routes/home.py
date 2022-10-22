from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi import APIRouter, Depends, HTTPException
from models.models import User , Expert, Trainer, Post, Story
from models.schemas import Email, Login, RegistrationIn, PostIn
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
    model = Post
    posts = model.whatTheUserFollows(user.id)
    return posts
    '''
    returns a list of stories based on the user's following list :)
    DB NOTE: add a user following and followers lists :)
    '''
    
    
# how to add 2 functions to the same endpoint?
# or should i simply merge them ?
@router.get('/home')
async def posts(user = Depends(get_user)):
    model = Post
    posts = model.whatTheUserFollows(user.id)
    return posts

@router.post('/home/create_post')
async def create_post(post : PostIn, user = Depends(get_user)):
    model = Post
    try:
           post_dict = reg_pydantic.dict(exclude_unset = False)
    except:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You missing some information!')
    v = await model.validate_post(post_dict, post_dict.keys())
    if v is not None:
        return v
    # save in database
    post = await model.create(**post_dict)
    await post.save()
    
'''
learn how to post likes and comments
'''

@router.post('/home/edit_post{id}')
async def edit_post(post : PostIn, user = Depends(get_user), post_id: int = Query()):
    model = Post
    post = await model.findById(id)
    if not post: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='error in finding the post')
    
    post_dict = reg_pydantic.dict(exclude_unset = False)
    v = await model.validate_post(post_dict, post_dict.keys())
    if v is not None:
        return v
    # save in database
    await model.edit(post_dict)
    return "done"
