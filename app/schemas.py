from pydantic import BaseModel

# Validate user data during creation.
class CreateUserSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True

# Structure user data when responding to API requests.
class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
