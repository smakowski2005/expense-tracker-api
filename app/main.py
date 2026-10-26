from fastapi import FastAPI
from app.database import engine, Base
from app.routes.expenses import router as expenses_router
from app.routes.users import router as users_router
from app import models

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(expenses_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Expense Tracker API"}