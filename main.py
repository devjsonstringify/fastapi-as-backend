import uvicorn

from fastapi import FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine
import models
import schemas

    
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
def create_todo(todo: schemas.ToDo):
    """_summary_"""
     # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = models.ToDo(task = todo.task)

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
    todo = session.query(models.ToDo).get(id)

    # close the session
    session.close()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.put("/todo/{id}")
def update_todo(id: int, task: str):
    """_summary_"""
     # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)
     # update todo item with the given task (if an item with the given id was found)
    if todo:
        todo.task = task
        session.commit()

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int):
    """_summary_"""

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None


@app.get("/todo")
def read_todo_list():
    """_summary_"""
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all todo items
    todo_list = session.query(models.ToDo).all()

    # close the session
    session.close()

    return todo_list

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
