"""
Starter code for the FastAPI REST APIs assignment.
Complete the TODOs to build a simple Todo API.
"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: Define a Pydantic model for Todo items
# It should have an 'id' field (int) and a 'title' field (str)
class Todo(BaseModel):
    id: int
    title: str


# In-memory storage for todos
todos = [
    {"id": 1, "title": "Learn FastAPI basics"},
    {"id": 2, "title": "Build your first API"},
    {"id": 3, "title": "Handle POST requests"}
]

# Track the next todo ID
next_id = 4


# TODO: Task 1 - Create a GET endpoint at the root path "/"
# It should return a dictionary with a welcome message
# Example: {"message": "Welcome to the Todo API"}
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}


# TODO: Task 1 - Create a GET endpoint at "/todos"
# It should return the list of todos
# Hint: Use @app.get("/todos") and return the todos list
@app.get("/todos")
def get_todos():
    return todos


# TODO: Task 2 - Create a POST endpoint at "/todos"
# It should:
# - Accept a Todo object in the request body
# - Add it to the todos list with a new ID
# - Return the created todo with status code 201
# Hint: Use @app.post("/todos", status_code=status.HTTP_201_CREATED)
# and accept a parameter of type Todo
@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo):
    global next_id
    new_todo = {"id": next_id, "title": todo.title}
    todos.append(new_todo)
    next_id += 1
    return new_todo


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
