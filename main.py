from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
from routes import register, home

from jose import JWTError, jwt
from fastapi import FastAPI, Depends, HTTPException, status , Body, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt

from passlib.hash import bcrypt
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(register.router, prefix = '/user', tags = ['home'])
app.include_router(home.router, prefix = '/home', tags = ['home'])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models.models']},
    generate_schemas=True,
    add_exception_handlers=True
)
