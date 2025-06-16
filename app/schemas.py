from pydantic import BaseModel, Field
from typing import Optional, List


class books(BaseModel):
    Book_name: str
    Tittle: str

class show_books(BaseModel):
    id: int
    Book_name: str
    Tittle: str

    class Config:
        from_attributes = True

class Users(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True

class show_user(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
        orm_mode = True


class Login(BaseModel):
    username: str = Field(..., alias='email')
    password: str

    class Config:
        from_attributes = True
        orm_mode = True
        allow_population_by_field_name = True



class TokenData(BaseModel):
    access_token: str
    token_type: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
