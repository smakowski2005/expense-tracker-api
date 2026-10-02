from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class ExpenseCreate(BaseModel):
    name: str
    amount: float = Field(...,gt=0)
    category: str
    date: date
    description: str | None = None

class ExpenseUpdate(ExpenseCreate):
    pass
class ExpenseResponse(ExpenseCreate):
    id: int
    pass
    model_config = ConfigDict(from_attributes=True)



