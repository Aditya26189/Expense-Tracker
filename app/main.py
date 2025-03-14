from fastapi import FastAPI
from .routes import expenses
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)  # for tables creation

app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])

@app.get("/")
def home():
    return {"message": "Welcome to Expense Tracker API"}
