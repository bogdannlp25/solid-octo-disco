# Frequently Asked Questions

## Database & Setup

### Q: "ModuleNotFoundError: No module named 'sqlalchemy'"

**A:** You need to install SQLAlchemy. Run:
```bash
pip install sqlalchemy
```

If you have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### Q: "sqlite3.OperationalError: database is locked"

**A:** Another program is using the database. Try:
1. Close any SQLite viewers (DB Browser, etc.)
2. Wait a few seconds
3. Try again

If still locked, delete `portfolio.db` and recreate it:
```bash
rm data/portfolio.db
python database.py
python sample_data.py
```

---

### Q: Can I use PostgreSQL instead of SQLite?

**A:** Yes! Change the DATABASE_URL in `database.py`:
```python
# SQLite (current)
DATABASE_URL = "sqlite:///./data/portfolio.db"

# PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost/portfolio_db"
```

You'll also need to install the driver:
```bash
pip install psycopg2
```

---

### Q: Where does my database file go?

**A:** By default, it's stored in `data/portfolio.db` (relative to your script). You can change this in `database.py`:
```python
DATABASE_URL = "sqlite:///./data/portfolio.db"  # Creates data/portfolio.db
DATABASE_URL = "sqlite:////tmp/portfolio.db"     # Creates /tmp/portfolio.db
```

---

## Models & Relationships

### Q: What's the difference between `relationship()` and `ForeignKey()`?

**A:**
- **ForeignKey()** - Database level constraint in the table definition
- **relationship()** - Python-level convenience to access related objects

Example:
```python
class Project(Base):
    __tablename__ = "projects"
    student_id = Column(Integer, ForeignKey("students.id"))  # DB constraint
    student = relationship("Student", back_populates="projects")  # Python convenience
```

Now you can do:
```python
project.student.name  # Access student through relationship
```

---

### Q: What does `back_populates` do?

**A:** It creates a two-way relationship. If you don't use it, you can only access:
```python
# Without back_populates
project.student  # Works
student.projects  # Doesn't work
```

With `back_populates`:
```python
# With back_populates
project.student  # Works
student.projects  # Also works!
```

---

### Q: What's `cascade="all, delete-orphan"`?

**A:** When you delete a student, what happens to their projects?

```python
# Without cascade
# If you delete a student, their projects remain in DB (orphaned)

# With cascade="all, delete-orphan"
# If you delete a student, their projects are automatically deleted too
```

---

## CRUD Operations

### Q: How do I query for all students with grade > 10?

**A:** Use SQLAlchemy's `.filter()` method:
```python
from sqlalchemy import and_, or_

# Simple filter
students = db.query(Student).filter(Student.grade > 10).all()

# Multiple conditions (AND)
students = db.query(Student).filter(
    and_(Student.grade > 10, Student.name.like("A%"))
).all()

# Multiple conditions (OR)
students = db.query(Student).filter(
    or_(Student.grade == 11, Student.grade == 12)
).all()
```

---

### Q: How do I sort results?

**A:** Use `.order_by()`:
```python
# Sort by name A-Z
students = db.query(Student).order_by(Student.name).all()

# Sort by grade Z-A (descending)
from sqlalchemy import desc
students = db.query(Student).order_by(desc(Student.grade)).all()
```

---

### Q: How do I limit results?

**A:** Use `.limit()`:
```python
# Get first 5 students
top_students = db.query(Student).limit(5).all()

# Get 10 students starting at position 20 (pagination)
page_2 = db.query(Student).offset(20).limit(10).all()
```

---

### Q: "sqlite3.IntegrityError: UNIQUE constraint failed: students.email"

**A:** You're trying to add a student with an email that already exists. Email must be unique!

```python
# This fails because email already exists
create_student(db, "Bob", "alice@school.edu", 11)

# Fix: Use a different email
create_student(db, "Bob", "bob@school.edu", 11)
```

---

### Q: How do I update multiple columns at once?

**A:** Pass all the changes:
```python
update_project(db, project_id, 
               title="New Title",
               grade_received=95,
               category="Web App")
```

---

### Q: What happens if I delete a student?

**A:** With `cascade="all, delete-orphan"`:
1. Student is deleted from Students table
2. All their projects are deleted from Projects table
3. All skills for those projects are deleted from SkillsUsed table

---

## Application & Testing

### Q: How do I run the CLI application?

**A:**
```bash
python main.py
```

Then follow the menu prompts.

---

### Q: How do I load sample data?

**A:**
```bash
python sample_data.py
```

This creates 2 students with 3 projects and multiple skills.

---

### Q: How do I clear all data and start fresh?

**A:**
```bash
# Delete the database
rm data/portfolio.db

# Reinitialize (creates empty database)
python database.py

# Load sample data again
python sample_data.py
```

---

### Q: How do I run the tests?

**A:** First install pytest:
```bash
pip install pytest
```

Then run:
```bash
pytest tests/
```

For verbose output:
```bash
pytest tests/ -v
```

---

### Q: "assert len(students) > 0" - test is failing

**A:** This means no students were found. Make sure:
1. Sample data was loaded: `python sample_data.py`
2. Database was created: `python database.py`
3. CRUD functions are working correctly

---

## FastAPI (Optional)

### Q: How do I create a FastAPI endpoint?

**A:** Add to your `api.py`:
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students/")
def list_students(db: Session = Depends(get_db)):
    return get_all_students(db)
```

---

### Q: How do I test my FastAPI endpoints?

**A:** Start the server:
```bash
uvicorn api:app --reload
```

Then test with curl:
```bash
curl http://localhost:8000/students/
```

Or visit in browser: `http://localhost:8000/docs`

---

## General Questions

### Q: How much code should I write?

**A:** You should write about 150-250 lines of code (not counting docstrings and comments). If you're under 100 lines, you're probably missing something. If you're over 400 lines, ask if you're overcomplicating things.

---

### Q: Can I add more tables?

**A:** Absolutely! Great extension. Try:
- **Reviews** table - students can review projects
- **Collaborations** table - track group projects
- **Certifications** table - track earned badges/certs

---

### Q: Can I change the scenario (not portfolio)?

**A:** Yes! The same schema works for:
- **Movie Database** (Movie, Actor, Genre)
- **Recipe Collection** (Recipe, Ingredient, Instruction)
- **Store Inventory** (Product, Category, Supplier)

Just adapt the table names and columns.

---

### Q: How should I commit to git?

**A:** Good practice:
```bash
git add -A
git commit -m "Initial database setup with models and CRUD operations"
git commit -m "Add sample data loader"
git commit -m "Add CLI application"
```

Don't commit `portfolio.db` - add to `.gitignore`:
```
*.db
__pycache__/
.env
```

---

### Q: Can I use an IDE or do I have to use the terminal?

**A:** Either works! Popular IDEs:
- **VS Code** (free, recommended)
- **PyCharm** (free Community Edition)
- **Thonny** (simple, great for learning)

Just make sure your IDE's Python environment has SQLAlchemy installed.

---

### Q: How do I know if my database is working?

**A:** Try this quick test:
```python
from database import SessionLocal, init_db
from crud_operations import *

init_db()
db = SessionLocal()

# Create a student
student = create_student(db, "Test", "test@email.com", 11)
print(f"Created student ID: {student.id}")

# Read them back
found = get_student_by_email(db, "test@email.com")
print(f"Found: {found.name}")

# Delete them
delete_student(db, student.id)
print("Deleted!")

db.close()
```

If this runs without errors, everything is working!

---

## Still Stuck?

1. **Read the error message** - it usually tells you what's wrong
2. **Check the ASSIGNMENT.md** - your answer is probably there
3. **Look at solutions/** - see how it's supposed to work
4. **Ask your instructor** - don't suffer alone!

---

**Last Updated:** November 2024
