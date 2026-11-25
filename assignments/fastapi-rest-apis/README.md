# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, a modern Python web framework. You'll create endpoints to handle GET and POST requests, work with request data, and return proper HTTP responses.

## 📝 Tasks

### 🛠️ Task 1: Create Your First API Endpoints

#### Description
Build the foundation of a Todo API by creating two basic GET endpoints. These endpoints will demonstrate how FastAPI handles routing and returns JSON responses.

#### Requirements
Your API should:

- Have a root endpoint (`GET /`) that returns a welcome message with the text "Welcome to the Todo API"
- Have a `/todos` endpoint (`GET /todos`) that returns a list of sample todo items (at least 3 items with `id` and `title` fields)
- Both endpoints should return valid JSON responses
- Run without errors when you start the server with `uvicorn main:app --reload`


### 🛠️ Task 2: Handle POST Requests and Create New Todos

#### Description
Extend your API to accept new todo items from clients. You'll learn how to process incoming request data, validate it, and add items to your list.

#### Requirements
Your API should:

- Have a `POST /todos` endpoint that accepts a new todo with a `title` field in the request body
- Automatically generate an `id` for each new todo (you can use a simple counter or auto-incrementing number)
- Add the new todo to your in-memory list and return the created todo with its ID and title
- Use Pydantic models to define the structure of todo items (use `BaseModel` for validation)
- Return an appropriate HTTP status code (201 Created) for successful POST requests
- Include basic validation so the title is required and cannot be empty

