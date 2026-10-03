from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate,UserResponse
from app.security import get_password_hash, verify_password,create_access_token
from fastapi.security import OAuth2PasswordRequestForm

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
@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user= db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token=create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}