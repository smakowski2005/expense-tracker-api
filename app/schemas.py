from pydantic import BaseModel, Field, ConfigDict, EmailStr
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
class UserCreate(BaseModel):
    email: EmailStr
    password: str
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)





