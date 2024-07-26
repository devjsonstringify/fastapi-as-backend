import uvicorn

from fastapi import FastAPI
from database import Base, engine
from pydantic import BaseModel

# Create the database
Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def read_root():
    """_summary_"""
    return {"Hello": "World"}

@app.get("/")
def root():
    """_summary_"""
    return "todooo"

@app.post("/todo")
def create_todo():
    """_summary_"""
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    """_summary_"""
    return "read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    """_summary_"""
    return "update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    """_summary_"""
    return "delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    """_summary_"""
    return "read todo list"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
