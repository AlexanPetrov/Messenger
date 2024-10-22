# Initializes the FastAPI app and link it with the routes

from fastapi import FastAPI
from .routes import router
from middleware.rate_limiter import rate_limit_handler
from slowapi.errors import RateLimitExceeded

app = FastAPI()

app.add_exception_handler(RateLimitExceeded, rate_limit_handler)

app.include_router(router)
