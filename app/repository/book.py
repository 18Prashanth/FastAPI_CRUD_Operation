from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from ..database import engine, sessionLocal
from .. import models

from app.logger import logger




def get_all(db: Session):
    db = sessionLocal()
    books = db.query(models.Book).all()
    if not books:
        db.close()
        return {"message": "No books found"}
    db.close()
    logger.info("Fetched all books successfully")
    return books

def get_book_id(id: int, db:Session):
    db = sessionLocal()
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")
    db.close()
    logger.info(f"Fetched book with ID {id} successfully")
    return book

def create(request: schemas.books, db: Session, current_user: models.User):
    db = sessionLocal()
    new_book = models.Book(Book_name=request.Book_name, Tittle=request.Tittle, user_id = current_user.id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()
    logger.info("Created new book successfully")
    return new_book

def delete(id: int, db:Session,current_user: models.User):
    db = sessionLocal()
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book.user_id != current_user.id:
        logger.error(f"Unauthorized attempt to delete book with ID {id} by user {current_user.id}")
        raise HTTPException(status_code=404, detail=f"Book {id} not found")
    db.delete(book)
    db.commit()
    db.close()
    logger.info("Deleted book with ID {id} successfully")
    return {"message": "Book deleted successfully"}

def update(id: int, request: schemas.books, db: Session,current_user: models.User):
    db = sessionLocal()
    existing_book = db.query(models.Book).filter(models.Book.id == id).first()
    if not existing_book or existing_book.user_id != current_user.id:
        raise HTTPException(status_code=404, detail=f"Book {id} not found")

    existing_book.Book_name = request.Book_name
    existing_book.Tittle = request.Tittle
    db.commit()
    db.refresh(existing_book)
    db.close()
    logger.info("Updated book with ID {id} successfully")
    return existing_book