from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    """_summary_"""
    task: str

class User(BaseModel):
    """_summary_"""
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    
class Token(BaseModel):
    """_summary_"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """_summary_"""
    username: str | None = None

class UserInDB(User):
    """_summary_"""
    hashed_password: str
