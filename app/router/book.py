from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..database import engine, sessionLocal
from app import database
from .. import schemas
from ..repository import book
from ..auth import oauth2

from app.logger import logger



router = APIRouter(
    tags=["Books"],
    prefix="/Book"
)

@router.get("/", status_code=status.HTTP_200_OK, tags=["Books"], response_model=List[schemas.show_books])
def get_all_books(db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    logger.info(f"Fetching all books for user {current_user.id}")
    return db.query(models.Book).filter(models.Book.user_id == current_user.id).all()

# @router.get('/{id}', status_code=status.HTTP_200_OK, tags=["Books"], response_model=schemas.show_books)
# def get_book_by_id(id: int, db: Session = Depends(database.get_db)):
#     return book.get_book_id(id, db)

@router.post("/", status_code=status.HTTP_201_CREATED, tags=["Books"])
def create_book(request: schemas.books, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    logger.info(f"Creating a new book for user {current_user.id}")
    return book.create(request, db,current_user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Books"])
def delete_book(id: int, db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    logger.info(f"Deleting book with ID {id} for user {current_user.id}")
    return book.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_200_OK, tags=["Books"], response_model=schemas.show_books)
def update_book(id: int, request: schemas.books, db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    logger.info(f"Updating book with ID {id} for user {current_user.id}")
    return book.update(id, request, db)