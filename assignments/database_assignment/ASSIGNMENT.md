# Assignment: Student Portfolio Database Manager

**Duration:** 2-3 weeks  
**Difficulty Level:** Intermediate  
**Prerequisites:** Python fundamentals, OOP, REST APIs (FastAPI)

---

## 🎯 Learning Objectives

By completing this assignment, you will:

1. **Design relational databases** using proper normalization and relationships
2. **Create SQLAlchemy ORM models** to represent database tables in Python
3. **Perform CRUD operations** (Create, Read, Update, Delete) using an ORM
4. **Write SQL queries** to retrieve and manipulate data
5. **Validate and persist data** to SQLite databases
6. **Connect a database to a FastAPI application** to build data-driven web services
7. **Implement relationships** between database entities (one-to-many, many-to-many)

---

## 📋 Project Overview

### Scenario

You're building a **Student Project Portfolio Manager** — a system where students can:
- Register and create profiles
- Track programming projects they've completed
- Organize projects by category/language
- Rate and review their projects
- Track project completion dates and outcomes

This is a **real-world application** that combines database design with the REST APIs you've already learned.

### Your Deliverable

You will create a Python application with:
- ✅ SQLite database with proper schema design
- ✅ SQLAlchemy ORM models with relationships
- ✅ CRUD operations (Python functions to Create, Read, Update, Delete)
- ✅ Data validation and error handling
- ✅ Optional: FastAPI endpoints to expose your database via REST API
- ✅ Sample data/fixtures for testing

---

## 🏗️ Database Schema Design

### Entity Relationship Diagram (ERD)

```
┌─────────────────────┐
│      Students       │
├─────────────────────┤
│ id (PK)             │
│ name                │
│ email (UNIQUE)      │
│ grade               │
│ joined_date         │
└──────────┬──────────┘
           │ (1:N)
           │
┌──────────▼──────────────────────┐
│        Projects                 │
├─────────────────────────────────┤
│ id (PK)                         │
│ student_id (FK → Students)      │
│ title                           │
│ description                     │
│ programming_language            │
│ category                        │
│ completion_date                 │
│ grade_received                  │
│ created_at                      │
└──────────┬──────────────────────┘
           │ (1:N)
           │
┌──────────▼──────────────────────┐
│        Skills_Used              │
├─────────────────────────────────┤
│ id (PK)                         │
│ project_id (FK → Projects)      │
│ skill_name                      │
└─────────────────────────────────┘
```

### Table Specifications

#### **Students Table**
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    grade INTEGER,
    joined_date TEXT DEFAULT CURRENT_TIMESTAMP,
    bio TEXT
);
```

**Columns:**
- `id`: Unique identifier (Primary Key)
- `name`: Student's full name
- `email`: Email address (must be unique)
- `grade`: Grade level (9-12)
- `joined_date`: When they joined (auto-populated)
- `bio`: Short biography/description

---

#### **Projects Table**
```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    programming_language TEXT,
    category TEXT,
    completion_date TEXT,
    grade_received REAL,
    github_url TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
```

**Columns:**
- `id`: Unique project identifier
- `student_id`: Reference to the student who created it
- `title`: Project name
- `description`: What the project does
- `programming_language`: Language used (Python, JavaScript, etc.)
- `category`: Type of project (Game, Web App, Data Analysis, etc.)
- `completion_date`: When finished
- `grade_received`: Grade/score (0-100)
- `github_url`: Link to code repository
- `created_at`: When added to portfolio

---

#### **Skills_Used Table** (Join Table)
```sql
CREATE TABLE skills_used (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    skill_name TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);
```

**Columns:**
- `id`: Unique identifier
- `project_id`: Which project used this skill
- `skill_name`: Name of the skill (OOP, APIs, Databases, etc.)

---

## 📂 Project Structure

Create the following folder structure:

```
portfolio_manager/
│
├── database.py              # Database initialization & setup
├── models.py                # SQLAlchemy ORM models
├── crud_operations.py       # CRUD functions
├── main.py                  # Main application logic
├── data/
│   ├── portfolio.db         # SQLite database (auto-created)
│   └── sample_data.py       # Sample data for testing
├── tests/
│   └── test_operations.py   # Unit tests (optional)
└── README.md                # Project documentation
```

---

## 🚀 Phase 1: Database Setup

### Task 1.1: Install Dependencies

```bash
pip install sqlalchemy
```

### Task 1.2: Create `database.py`

This file initializes your database connection:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Create database URL (using SQLite)
DATABASE_URL = "sqlite:///./data/portfolio.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    """Generator function to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database - create all tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()
```

### Task 1.3: Run Database Initialization

```bash
python database.py
```

This creates your SQLite database in `data/portfolio.db`.

---

## 🏢 Phase 2: Create ORM Models

### Task 2.1: Create `models.py`

Define your SQLAlchemy models (Python classes that map to database tables):

```python
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Student(Base):
    """Student model - represents a student in the portfolio system"""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    grade = Column(Integer)  # 9-12
    bio = Column(Text)
    joined_date = Column(String, default=str(datetime.now()))
    
    # Relationship: one student has many projects
    projects = relationship("Project", back_populates="student", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"


class Project(Base):
    """Project model - represents a project in a student's portfolio"""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    programming_language = Column(String(50))
    category = Column(String(50))  # Game, Web App, Data Analysis, etc.
    completion_date = Column(String)
    grade_received = Column(Float)  # 0-100
    github_url = Column(String(255))
    created_at = Column(String, default=str(datetime.now()))
    
    # Relationships
    student = relationship("Student", back_populates="projects")
    skills = relationship("SkillUsed", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Project(id={self.id}, title='{self.title}', student_id={self.student_id})>"


class SkillUsed(Base):
    """SkillUsed model - tracks skills used in each project"""
    __tablename__ = "skills_used"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    skill_name = Column(String(100), nullable=False)
    
    # Relationship
    project = relationship("Project", back_populates="skills")
    
    def __repr__(self):
        return f"<SkillUsed(id={self.id}, skill='{self.skill_name}', project_id={self.project_id})>"
```

**Key Concepts:**
- `__tablename__`: Name of the database table
- `Column()`: Database columns with types (Integer, String, etc.)
- `ForeignKey()`: Links to another table
- `relationship()`: Python-level connection between models
- `cascade="all, delete-orphan"`: If a student is deleted, their projects are too

---

## ⚙️ Phase 3: CRUD Operations

### Task 3.1: Create `crud_operations.py`

```python
from sqlalchemy.orm import Session
from models import Student, Project, SkillUsed
from datetime import datetime

# ==================== CREATE OPERATIONS ====================

def create_student(db: Session, name: str, email: str, grade: int, bio: str = None) -> Student:
    """Create a new student"""
    student = Student(name=name, email=email, grade=grade, bio=bio)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def create_project(db: Session, student_id: int, title: str, description: str = None, 
                   language: str = None, category: str = None, 
                   completion_date: str = None, grade: float = None, 
                   github_url: str = None) -> Project:
    """Create a new project for a student"""
    project = Project(
        student_id=student_id,
        title=title,
        description=description,
        programming_language=language,
        category=category,
        completion_date=completion_date,
        grade_received=grade,
        github_url=github_url
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def add_skill_to_project(db: Session, project_id: int, skill_name: str) -> SkillUsed:
    """Add a skill to a project"""
    skill = SkillUsed(project_id=project_id, skill_name=skill_name)
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


# ==================== READ OPERATIONS ====================

def get_student_by_id(db: Session, student_id: int) -> Student:
    """Get a student by ID"""
    return db.query(Student).filter(Student.id == student_id).first()


def get_student_by_email(db: Session, email: str) -> Student:
    """Get a student by email"""
    return db.query(Student).filter(Student.email == email).first()


def get_all_students(db: Session) -> list[Student]:
    """Get all students"""
    return db.query(Student).all()


def get_project_by_id(db: Session, project_id: int) -> Project:
    """Get a project by ID"""
    return db.query(Project).filter(Project.id == project_id).first()


def get_student_projects(db: Session, student_id: int) -> list[Project]:
    """Get all projects for a specific student"""
    return db.query(Project).filter(Project.student_id == student_id).all()


def get_projects_by_language(db: Session, language: str) -> list[Project]:
    """Get all projects written in a specific language"""
    return db.query(Project).filter(Project.programming_language == language).all()


def get_projects_by_category(db: Session, category: str) -> list[Project]:
    """Get all projects in a specific category"""
    return db.query(Project).filter(Project.category == category).all()


def get_project_skills(db: Session, project_id: int) -> list[SkillUsed]:
    """Get all skills used in a project"""
    return db.query(SkillUsed).filter(SkillUsed.project_id == project_id).all()


# ==================== UPDATE OPERATIONS ====================

def update_student(db: Session, student_id: int, **kwargs) -> Student:
    """Update a student's information"""
    student = get_student_by_id(db, student_id)
    if student:
        for key, value in kwargs.items():
            if hasattr(student, key) and value is not None:
                setattr(student, key, value)
        db.commit()
        db.refresh(student)
    return student


def update_project(db: Session, project_id: int, **kwargs) -> Project:
    """Update a project"""
    project = get_project_by_id(db, project_id)
    if project:
        for key, value in kwargs.items():
            if hasattr(project, key) and value is not None:
                setattr(project, key, value)
        db.commit()
        db.refresh(project)
    return project


# ==================== DELETE OPERATIONS ====================

def delete_student(db: Session, student_id: int) -> bool:
    """Delete a student (and all their projects)"""
    student = get_student_by_id(db, student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False


def delete_project(db: Session, project_id: int) -> bool:
    """Delete a project"""
    project = get_project_by_id(db, project_id)
    if project:
        db.delete(project)
        db.commit()
        return True
    return False


def delete_skill(db: Session, skill_id: int) -> bool:
    """Delete a skill from a project"""
    skill = db.query(SkillUsed).filter(SkillUsed.id == skill_id).first()
    if skill:
        db.delete(skill)
        db.commit()
        return True
    return False


# ==================== ANALYTICS ====================

def get_student_stats(db: Session, student_id: int) -> dict:
    """Get statistics for a student's portfolio"""
    student = get_student_by_id(db, student_id)
    if not student:
        return None
    
    projects = get_student_projects(db, student_id)
    
    return {
        "student_name": student.name,
        "total_projects": len(projects),
        "avg_grade": sum(p.grade_received for p in projects if p.grade_received) / len([p for p in projects if p.grade_received]) if any(p.grade_received for p in projects) else 0,
        "languages_used": list(set(p.programming_language for p in projects if p.programming_language)),
        "categories": list(set(p.category for p in projects if p.category))
    }
```

---

## 🧪 Phase 4: Testing Your Database

### Task 4.1: Create `sample_data.py`

Load test data to verify everything works:

```python
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from crud_operations import *

def load_sample_data():
    """Load sample data into the database"""
    db = SessionLocal()
    
    # Clear existing data
    db.query(Student).delete()
    
    print("📥 Loading sample data...")
    
    # Create students
    student1 = create_student(
        db,
        name="Alice Johnson",
        email="alice@school.edu",
        grade=11,
        bio="Aspiring software engineer"
    )
    
    student2 = create_student(
        db,
        name="Bob Smith",
        email="bob@school.edu",
        grade=10,
        bio="Game development enthusiast"
    )
    
    print(f"✅ Created {student1.name} and {student2.name}")
    
    # Create projects for Alice
    project1 = create_project(
        db,
        student_id=student1.id,
        title="Python Adventure Game",
        description="Text-based adventure game with player choices",
        language="Python",
        category="Game",
        completion_date="2024-10-15",
        grade=95,
        github_url="https://github.com/alice/adventure-game"
    )
    
    # Add skills to project1
    add_skill_to_project(db, project1.id, "OOP")
    add_skill_to_project(db, project1.id, "File I/O")
    
    project2 = create_project(
        db,
        student_id=student1.id,
        title="Data Analysis Dashboard",
        description="Analyze student grades and generate reports",
        language="Python",
        category="Data Analysis",
        completion_date="2024-11-20",
        grade=92,
        github_url="https://github.com/alice/data-dashboard"
    )
    
    add_skill_to_project(db, project2.id, "Pandas")
    add_skill_to_project(db, project2.id, "Matplotlib")
    
    # Create projects for Bob
    project3 = create_project(
        db,
        student_id=student2.id,
        title="2D Platformer Game",
        description="Simple platformer game with enemies and collectibles",
        language="Python",
        category="Game",
        completion_date="2024-11-10",
        grade=88,
        github_url="https://github.com/bob/platformer"
    )
    
    add_skill_to_project(db, project3.id, "Pygame")
    add_skill_to_project(db, project3.id, "Game Logic")
    
    print(f"✅ Created {project1.title}, {project2.title}, {project3.title}")
    
    # Test queries
    print("\n🧪 Testing queries...")
    
    # Get student and their projects
    alice = get_student_by_email(db, "alice@school.edu")
    print(f"\n📌 {alice.name}'s Projects:")
    for proj in alice.projects:
        print(f"  - {proj.title} ({proj.category}) - Grade: {proj.grade_received}")
    
    # Get stats
    stats = get_student_stats(db, alice.id)
    print(f"\n📊 {alice.name}'s Stats:")
    print(f"  Total Projects: {stats['total_projects']}")
    print(f"  Average Grade: {stats['avg_grade']:.1f}")
    print(f"  Languages: {', '.join(stats['languages_used'])}")
    
    # Find Python projects
    python_projects = get_projects_by_language(db, "Python")
    print(f"\n🐍 All Python Projects: {len(python_projects)}")
    for proj in python_projects:
        print(f"  - {proj.title}")
    
    db.close()
    print("\n✅ Sample data loaded successfully!")


if __name__ == "__main__":
    init_db()
    load_sample_data()
```

### Task 4.2: Run Sample Data Script

```bash
python sample_data.py
```

You should see output like:
```
📥 Loading sample data...
✅ Created Alice Johnson and Bob Smith
✅ Created Python Adventure Game, Data Analysis Dashboard, 2D Platformer Game
...
✅ Sample data loaded successfully!
```

---

## 🎯 Phase 5: Main Application

### Task 5.1: Create `main.py`

A simple CLI interface to interact with your database:

```python
from database import SessionLocal, init_db
from crud_operations import *

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("📚 Student Portfolio Manager")
    print("="*50)
    print("1. Add a new student")
    print("2. View all students")
    print("3. Add a project")
    print("4. View student projects")
    print("5. View student statistics")
    print("6. Update a project grade")
    print("7. Exit")
    print("="*50)


def main():
    """Main application loop"""
    init_db()
    db = SessionLocal()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            # Add student
            name = input("Student name: ").strip()
            email = input("Email: ").strip()
            grade = int(input("Grade (9-12): ").strip())
            bio = input("Bio (optional): ").strip()
            
            student = create_student(db, name, email, grade, bio)
            print(f"✅ Student {student.name} added with ID {student.id}")
        
        elif choice == "2":
            # View all students
            students = get_all_students(db)
            if not students:
                print("No students found.")
            else:
                print(f"\n📌 Total Students: {len(students)}")
                for s in students:
                    print(f"  ID: {s.id} | {s.name} ({s.email}) | Grade: {s.grade}")
        
        elif choice == "3":
            # Add project
            student_id = int(input("Student ID: ").strip())
            title = input("Project title: ").strip()
            description = input("Description: ").strip()
            language = input("Programming language: ").strip()
            category = input("Category (Game/Web App/Data Analysis/etc): ").strip()
            
            project = create_project(db, student_id, title, description, language, category)
            print(f"✅ Project '{project.title}' added with ID {project.id}")
            
            # Add skills
            while True:
                skill = input("Add a skill (or press Enter to skip): ").strip()
                if not skill:
                    break
                add_skill_to_project(db, project.id, skill)
                print(f"  ✅ Skill '{skill}' added")
        
        elif choice == "4":
            # View projects
            student_id = int(input("Student ID: ").strip())
            projects = get_student_projects(db, student_id)
            if not projects:
                print("This student has no projects yet.")
            else:
                print(f"\n📁 Projects ({len(projects)} total):")
                for p in projects:
                    print(f"  ID: {p.id} | {p.title} ({p.category}) - {p.programming_language}")
                    if p.skills:
                        skills_list = ", ".join([s.skill_name for s in p.skills])
                        print(f"    Skills: {skills_list}")
                    if p.grade_received:
                        print(f"    Grade: {p.grade_received}")
        
        elif choice == "5":
            # View statistics
            student_id = int(input("Student ID: ").strip())
            stats = get_student_stats(db, student_id)
            if stats:
                print(f"\n📊 Statistics for {stats['student_name']}:")
                print(f"  Total Projects: {stats['total_projects']}")
                print(f"  Average Grade: {stats['avg_grade']:.1f}")
                print(f"  Languages: {', '.join(stats['languages_used'])}")
                print(f"  Categories: {', '.join(stats['categories'])}")
            else:
                print("Student not found.")
        
        elif choice == "6":
            # Update project grade
            project_id = int(input("Project ID: ").strip())
            new_grade = float(input("New grade (0-100): ").strip())
            project = update_project(db, project_id, grade_received=new_grade)
            if project:
                print(f"✅ Project grade updated to {project.grade_received}")
            else:
                print("Project not found.")
        
        elif choice == "7":
            print("👋 Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    db.close()


if __name__ == "__main__":
    main()
```

### Task 5.2: Run the Application

```bash
python main.py
```

---

## 🌐 (Optional) Phase 6: Integrate with FastAPI

If you want to expose your database via REST API:

### Task 6.1: Create API Endpoints

```python
# requirements.txt additions:
# fastapi
# uvicorn

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from crud_operations import *
from models import Student, Project

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all students
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return get_all_students(db)

# GET student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_id)
    if not student:
        return {"error": "Student not found"}
    return student

# POST new student
@app.post("/students/")
def create_new_student(name: str, email: str, grade: int, db: Session = Depends(get_db)):
    return create_student(db, name, email, grade)

# GET student's projects
@app.get("/students/{student_id}/projects/")
def get_student_portfolio(student_id: int, db: Session = Depends(get_db)):
    return get_student_projects(db, student_id)

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run with: `uvicorn api:app --reload`

---

## ✅ Submission Checklist

Before submitting, verify that your code:

- [ ] Database initializes without errors
- [ ] All models are defined (Student, Project, SkillUsed)
- [ ] CRUD operations work correctly
- [ ] Sample data loads successfully
- [ ] You can query students, projects, and skills
- [ ] Update and delete operations work
- [ ] Code is well-commented
- [ ] `README.md` explains how to run your code
- [ ] No syntax errors or import issues

---

## 📊 Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Database Schema** | 20 | Proper normalization, relationships, appropriate data types |
| **Models & ORM** | 20 | Correct SQLAlchemy models, relationships defined |
| **CRUD Operations** | 20 | All Create, Read, Update, Delete functions work correctly |
| **Data Validation** | 10 | Proper constraints (unique emails, not nulls, etc.) |
| **Code Quality** | 15 | Well-organized, documented, follows Python conventions |
| **Testing & Demo** | 15 | Sample data loads, queries return correct results |

**Total: 100 points**

---

## 🚀 Extension Challenges (For A+ Work)

### Challenge 1: Advanced Queries
Implement these functions in `crud_operations.py`:
- Get all students with average grade > 90
- Find the most used programming language across all projects
- Get projects completed within a date range
- Find skills used in multiple projects (popularity ranking)

### Challenge 2: Relationships
Add a new feature:
- **Collaborations Table**: Track when multiple students worked together on a project
- Modify `SkillUsed` to become a many-to-many relationship between Projects and Skills

### Challenge 3: Data Validation
- Add validators to ensure grades are between 0-100
- Ensure emails match a valid format
- Prevent duplicate skill entries in the same project

### Challenge 4: Performance
- Add database indexes for frequently queried columns (email, language, category)
- Implement pagination for the `get_all_students()` and `get_all_projects()` functions

### Challenge 5: Reporting
Create a `reports.py` file with functions to generate:
- Portfolio summary PDF or text report for each student
- Comparison statistics between students
- Language/category popularity across all portfolios

---

## 📚 Resources

- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org/
- **SQLite Documentation**: https://www.sqlite.org/docs.html
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Python ORM Tutorial**: https://realpython.com/python-sqlite-sqlalchemy/

---

## ❓ Common Questions

**Q: Can I use PostgreSQL instead of SQLite?**
A: Yes! Change the DATABASE_URL to: `postgresql://user:password@localhost/portfolio_db`

**Q: Do I need to know SQL?**
A: SQLAlchemy handles most SQL for you. But learning basic SQL helps you write better queries.

**Q: What if I delete a student? Do their projects delete too?**
A: Yes! We set `cascade="all, delete-orphan"` in the relationship, so deleting a student automatically deletes their projects.

**Q: Can I add more tables?**
A: Absolutely! Try adding a `Reviews` table where students can review projects, or a `Certifications` table.

---

Good luck! 🚀 You're building real-world database skills!
