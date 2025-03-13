from fastapi import FastAPI
from app.routes import expenses
app = FastAPI()

@app.get("/")  
def home():
    return {"message": "Welcome to the Expense Tracker!"}


app.include_router(expenses.router)