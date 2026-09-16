from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.schemas import ExpenseCreate

router = APIRouter()

@router.post("/expenses")
def create_expense(
        expense: ExpenseCreate,
        db: Session = Depends(get_db)
):
    new_expense = Expense(
        name=expense.name,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
        description=expense.description
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
@router.get("/expenses")
def read_expenses(name: Optional[str] = None,db: Session = Depends(get_db)):
    query=db.query(Expense)
    if name is not None:
        query = query.filter(Expense.name.ilike(f"%{name}%"))
    expenses = query.all()
    return expenses