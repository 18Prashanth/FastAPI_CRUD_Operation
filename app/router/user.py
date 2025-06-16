from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..repository import user

from app.logger import logger



router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get('/{id}', response_model = schemas.show_user, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching user with ID {id}")
    return user.get_user(id, db)


@router.post('/')
def register(request: schemas.Users,db: Session = Depends(get_db)):
    logger.info("Creating a new user")
    return user.user_create(request, db)


@router.post('/login', response_model=schemas.TokenResponse, status_code=status.HTTP_200_OK)
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.info("User login attempt")
    return user.login(request, db)