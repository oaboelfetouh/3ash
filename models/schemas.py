from fastapi import Body
from pydantic import BaseModel


class RegistrationIn(BaseModel):
    email: str = Body(..., example = "3amori@gmail.com")
    username: str = Body(..., example="Omar Aboelfetouh")
    password: str = Body(..., example = "star12")
    Password_Again: str = Body(..., example = "star12")
    

class Login(BaseModel):
    email: str = Body(..., example = "3amori@gmail.com")
    password: str = Body(..., example = "star12")

class Email(BaseModel):
    email: str = Body(..., example = "3amori@gmail.com")

class NewPassword(BaseModel):
    password: str = Body(..., example = "star12")
    password_again: str = Body(..., example = "star12")

class PostIn(BaseModel):
    text: str = Body(..., example = "What do you want to share?")
    picture: str = Body(..., example = "add a picture link")
