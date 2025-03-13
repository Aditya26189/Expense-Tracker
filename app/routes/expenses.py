from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Expense

router = APIRouter()

@router.get("/expenses")
# def get_expenses(db: Session = Depends(get_db)):
#     return db.query(Expense).all()
def print():
    return {"Hello, World!"}
