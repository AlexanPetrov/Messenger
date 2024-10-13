# Initializes the FastAPI app and link it with the routes

from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router)
