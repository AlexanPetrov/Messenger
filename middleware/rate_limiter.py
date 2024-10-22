from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.responses import JSONResponse

# Initialize Limiter
limiter = Limiter(key_func=get_remote_address)

# Exception handling for rate limit exceeded
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded"}
    )
