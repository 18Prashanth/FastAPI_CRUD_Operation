from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True, index=True)
    Book_name = Column(String)
    Tittle = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))

    owner = relationship("User", back_populates="books")

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    books = relationship("Book", back_populates="owner")