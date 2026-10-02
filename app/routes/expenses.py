from http.client import HTTPException
from os import name
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseUpdate

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
@router.post("/expenses/{expense_id}")
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="ID not found")
    else:
        return expense

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if expense is not None:
            db.delete(expense)
            db.commit()
            db.refresh(expense)
        else:
            raise HTTPException(status_code=404, detail="ID not found")


@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int,expense_data: ExpenseUpdate,db: Session = Depends(get_db)):
        expense = (db.query(Expense).filter(Expense.id == expense_id).first())
        if not expense:
            raise HTTPException(status_code=404, detail="ID not found")
        expense.name = expense_data.name
        expense.amount = expense_data.amount
        expense.category = expense_data.category
        expense.date = expense_data.date
        expense.description = expense_data.description
        db.commit()
        db.refresh(expense)
        return expense