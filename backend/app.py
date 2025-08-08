"""FAST API Initialization"""

from fastapi import FastAPI

from backend.main import main_app

app = FastAPI(title="PersonalFinance")
app.include_router(main_app)
