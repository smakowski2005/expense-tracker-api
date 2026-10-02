from pydantic import BaseModel, Field
from datetime import date

class ExpenseCreate(BaseModel):
    name: str
    amount: float = Field(...,gt=0)
    category: str
    date: date
    description: str | None = None

class ExpenseUpdate(ExpenseCreate):
    pass


