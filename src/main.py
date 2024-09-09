from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from . import models
from .config import get_settings
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world(request: Request, db: Session = Depends(get_db)):
    return "Hello World!"
