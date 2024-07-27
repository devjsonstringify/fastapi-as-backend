import uvicorn

from fastapi import FastAPI, status, HTTPException
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    task: str
    
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

@app.post("/todo", status_code=status.HTTP_201_CREATED, description="create todo.")
def create_todo(todo: ToDoRequest):
    """_summary_"""
     # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # grab the id given to the object from the database
    id = tododb.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"

@app.get("/todo/{id}")
def read_todo(id: int):
    """_summary_"""
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # close the session
    session.close()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

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
