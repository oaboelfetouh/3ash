from fastapi import Body
from pydantic import BaseModel


class RegistrationIn(BaseModel):
    email: str = Body(..., example = "3amori@gmail.com")
    username: str = Body(..., example="Omar Aboelfetouh")
    password: str = Body(..., example = "star12")
    Password_Again = Body(..., example = "star12")
    def verifyEmailAndUsername(self):
        return True
        # if the mail/user in the database return false
    def verify_password_length(self):
        if len(self.password) < 8:
            return False
        return True
    def verify_password_again(self):
        if self.password != self.Password_Again:
            return False
        return True
    

class Login(BaseModel):
    email: str = Body(..., example = "3amori@gmail.com")
    password: str = Body(..., example = "star12")
