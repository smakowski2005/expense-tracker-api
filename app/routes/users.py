from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate,UserResponse
from app.security import get_password_hash

router = APIRouter()
@router.post("/users/",response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    query = db.query(User).filter(User.email == user_data.email).first()
    if query:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user