from fastapi import HTTPException
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseUpdate, ExpenseResponse

router = APIRouter()

@router.post("/expenses",response_model=ExpenseResponse)
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
@router.get("/expenses",response_model=list[ExpenseResponse])
def read_expenses(name: Optional[str] = None, category: Optional[str] = None,skip: int = 0,limit: int = 100,db: Session = Depends(get_db)):
    query=db.query(Expense)
    if name:
        query = query.filter(Expense.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Expense.category == category)
    expenses = query.offset(skip).limit(limit).all()
    return expenses
@router.get("/expenses/{expense_id}",response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="ID not found")
    else:
        return expense

@router.put("/expenses/{expense_id}",response_model=ExpenseResponse)
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
@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="ID not found")
    db.delete(expense)
    db.commit()
    return {"message": f"Expense deleted successfully"}