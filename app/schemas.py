from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str
    date: date
    description: str | None = None

