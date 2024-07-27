from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    """_summary_"""
    task: str
