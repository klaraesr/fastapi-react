from typing import Optional
from pydantic import BaseModel,EmailStr


#properties required during user creation
class UserCreate(BaseModel):
    username: str
    email : EmailStr
    password : str
    class Config:
        schema_extra = {
            "example": {
                "username": "Klara Bar",
                "email": "klara@bar.com",
                "password": "secret123",
            }
        }

class ShowUser(BaseModel):
    username : str 
    email : EmailStr
    is_active : bool

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True