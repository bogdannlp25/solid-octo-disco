# FastAPI REST APIs Assignment - Requirements

This assignment requires the following Python packages:

- fastapi>=0.68.0
- uvicorn>=0.15.0
- pydantic>=1.8.0

## Installation

Install the required packages using pip:

```bash
pip install fastapi uvicorn pydantic
```

## Running the API

To start your API server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

You can explore the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing Your API

You can test your endpoints using curl or any HTTP client:

```bash
# Test GET /
curl http://localhost:8000/

# Test GET /todos
curl http://localhost:8000/todos

# Test POST /todos
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "My new todo", "id": 0}'
```

