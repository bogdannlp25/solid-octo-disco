# Getting Started Guide

**Don't feel overwhelmed!** This guide will walk you through the assignment step-by-step.

## 🎬 Before You Start (5 minutes)

### 1. Install Python 3.8+

Check your version:
```bash
python --version
```

Should show `Python 3.8` or higher.

### 2. Set Up a Project Folder

```bash
mkdir my_portfolio_project
cd my_portfolio_project
```

### 3. Download Starter Code

Copy the files from the `starter_template/` folder in this assignment.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `sqlalchemy` - Database ORM
- `pytest` - For testing (optional)

## 🚀 Week 1: Database & Models

### Day 1-2: Setup Database

1. **Read** ASSIGNMENT.md Phase 1 (Database Setup)
2. **Copy** `database.py` to your project
3. **Run it:**
   ```bash
   python database.py
   ```
4. **Verify:** A `portfolio.db` file appears in `data/` folder

✅ **Checkpoint:** You have a database!

### Day 3-4: Create Models

1. **Read** ASSIGNMENT.md Phase 2 (ORM Models)
2. **Copy** `models.py` to your project
3. **Review** the Student, Project, and SkillUsed classes
4. **Understand:**
   - What is `__tablename__`?
   - What do `Column()` and `relationship()` do?
5. **Don't modify yet** - just understand it

✅ **Checkpoint:** You understand database relationships!

### Day 5-7: Test It Out

1. **Copy** `sample_data.py` to your project
2. **Run it:**
   ```bash
   python sample_data.py
   ```
3. **Look at output** - does it show students and projects?
4. **Check database:** Open `portfolio.db` in a SQLite viewer
   - Try: [DB Browser for SQLite](https://sqlitebrowser.org/)

✅ **Week 1 Done:** Database is working with real data!

---

## 🎯 Week 2: CRUD Operations

### Day 8-10: Implement Create & Read

1. **Read** ASSIGNMENT.md Phase 3 (CRUD Operations)
2. **Copy** `crud_operations.py` to your project
3. **Study** these functions first:
   - `create_student()`
   - `get_student_by_id()`
   - `get_all_students()`
4. **Don't copy-paste blindly** - type out the code, understand each line

### Day 11-13: Implement Update & Delete

1. **Study** in `crud_operations.py`:
   - `update_student()`
   - `delete_student()`
   - `delete_project()`
2. **Ask yourself:** Why does deleting a student also delete projects?
3. **Test manually:**
   ```python
   from database import SessionLocal
   from crud_operations import *
   
   db = SessionLocal()
   alice = get_student_by_email(db, "alice@school.edu")
   print(alice.name)
   ```

✅ **Week 2 Done:** You can Create, Read, Update, Delete data!

---

## 🎮 Week 3: Application & Testing

### Day 14-15: CLI Application

1. **Copy** `main.py` to your project
2. **Run it:**
   ```bash
   python main.py
   ```
3. **Try the menu:**
   - Add a new student
   - View all students
   - Add a project
4. **Play with it** - make sure all features work

### Day 16-18: Run Tests

1. **Copy** test files from `tests/` folder
2. **Install pytest:**
   ```bash
   pip install pytest
   ```
3. **Run tests:**
   ```bash
   pytest tests/
   ```
4. **Fix any failures** - read error messages carefully

✅ **Week 3 Done:** Your application is working!

---

## 🚀 Optional: Add FastAPI

If you want to build REST API endpoints:

1. **Install FastAPI:**
   ```bash
   pip install fastapi uvicorn
   ```

2. **Create `api.py`** (copy from ASSIGNMENT.md Phase 6)

3. **Run server:**
   ```bash
   uvicorn api:app --reload
   ```

4. **Test endpoint:**
   ```bash
   curl http://localhost:8000/students/
   ```

---

## ✅ Submission Checklist

Before you submit, verify:

- [ ] `database.py` creates database without errors
- [ ] `models.py` defines all 3 models (Student, Project, SkillUsed)
- [ ] `sample_data.py` runs and loads data
- [ ] `crud_operations.py` has all CRUD functions
- [ ] `main.py` menu works (add student, view, add project, etc.)
- [ ] All tests pass: `pytest tests/`
- [ ] Code is commented
- [ ] `README.md` explains how to run your code
- [ ] No syntax errors (check with: `python -m py_compile *.py`)

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'sqlalchemy'"

**Fix:** Install dependencies
```bash
pip install -r requirements.txt
```

### "Database is locked"

**Fix:** Close any other programs using the database, then try again

### "Foreign key constraint failed"

**Fix:** You're trying to create a project for a non-existent student. Create the student first!

### Tests fail

**Fix:** 
1. Read the error message carefully
2. Check your CRUD functions match the expected output
3. Look at `solutions/` folder for reference
4. Ask for help!

### "sqlite3.IntegrityError: UNIQUE constraint failed"

**Fix:** You're trying to add a student with an email that already exists. Use a different email.

---

## 💡 Tips for Success

1. **Don't rush** - take time to understand each concept
2. **Test constantly** - run code after each change
3. **Read error messages** - they tell you what's wrong!
4. **Use the reference solutions** - look at how things are done
5. **Ask questions** - don't get stuck for hours
6. **Comment your code** - help yourself (and your grader!) understand it
7. **Start early** - don't wait until the day before!

---

## 📚 Additional Resources

- **SQLAlchemy Tutorial:** https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- **SQLite Browser:** https://sqlitebrowser.org/
- **Database Normalization:** https://www.youtube.com/watch?v=UrYkZJ1-7Q0
- **FastAPI Tutorial:** https://fastapi.tiangolo.com/tutorial/

---

**Questions?** Check [FAQS.md](./FAQS.md) or ask your instructor!

Good luck! You've got this! 🚀
