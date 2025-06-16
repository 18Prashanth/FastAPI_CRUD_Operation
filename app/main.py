from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi import status
from . import models
from sqlalchemy.orm import Session
from .database import engine
from .router import book, user
from .database import get_db
from . import schemas


app = FastAPI()

from fastapi import Request
from fastapi.responses import JSONResponse
from app.logger import logger

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

models.Base.metadata.create_all(engine)
app.include_router(book.router)
app.include_router(user.router)







