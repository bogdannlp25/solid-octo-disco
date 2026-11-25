# Student Portfolio Database Manager - Assignment Materials

This folder contains all resources for the **Student Portfolio Database Manager** assignment.

## 📂 Folder Structure

```
database_assignment/
├── README.md                          # This file
├── ASSIGNMENT.md                      # Full assignment description
├── RUBRIC.md                          # Grading rubric
├── GETTING_STARTED.md                 # Quick start guide
├── starter_template/                  # Starter code template
│   ├── database.py
│   ├── models.py
│   ├── crud_operations.py
│   ├── main.py
│   ├── sample_data.py
│   ├── requirements.txt
│   └── README.md
├── solutions/                         # Reference solutions
│   ├── database.py
│   ├── models.py
│   ├── crud_operations.py
│   ├── main.py
│   └── sample_data.py
├── tests/                             # Test cases students should pass
│   ├── test_models.py
│   ├── test_crud.py
│   └── test_queries.py
└── FAQS.md                            # Common student questions
```

## 🎯 Assignment Overview

**Duration:** 2-3 weeks  
**Difficulty:** Intermediate  
**Skills:** Databases, SQL, SQLAlchemy ORM, Python, Data Persistence

Students build a database-backed portfolio management system that:
- Stores student profiles and project information
- Implements CRUD operations with SQLAlchemy
- Demonstrates relational database design
- Optionally integrates with REST APIs (FastAPI)

## 📚 For Students

1. **Start Here:** Read [GETTING_STARTED.md](./GETTING_STARTED.md)
2. **Understand Assignment:** Read [ASSIGNMENT.md](./ASSIGNMENT.md)
3. **Use Starter Code:** Copy files from `starter_template/`
4. **Follow Phases:** Complete Phase 1 through Phase 5
5. **Test Your Work:** Run tests in `tests/` folder
6. **Check Rubric:** Review [RUBRIC.md](./RUBRIC.md) before submitting

## 👨‍🏫 For Instructors

### Setup Instructions

1. **Copy Assignment to Website**
   ```bash
   # Update config.json to reference this assignment
   ```

2. **Review Solutions** in `solutions/` folder for grading

3. **Run Test Suite**
   ```bash
   pip install pytest
   pytest tests/
   ```

### Customization

- **Adjust Duration:** Change timeline in ASSIGNMENT.md
- **Modify Points:** Update grading weights in RUBRIC.md
- **Add Extensions:** Add custom challenges in ASSIGNMENT.md
- **Change Scenario:** Adapt "Student Portfolio" to your context (e.g., "Movie Database", "Recipe Collection")

### Key Dates to Set

- Assignment Release Date
- Checkpoint 1 (Phase 1-2 complete)
- Checkpoint 2 (Phase 1-4 complete)
- Final Submission Deadline

## 💾 Database Schema Quick Reference

```
Students (1) ──── (N) Projects ──── (N) SkillsUsed
   • id              • id              • id
   • name            • student_id      • project_id
   • email           • title           • skill_name
   • grade           • description
   • bio             • language
                     • category
                     • grade_received
```

## ⚙️ Tech Stack

- **Language:** Python 3.8+
- **Database:** SQLite (or PostgreSQL)
- **ORM:** SQLAlchemy
- **Optional API:** FastAPI
- **Testing:** pytest

## 🚀 Quick Start

For instructors who want to preview:
```bash
cd starter_template/
pip install -r requirements.txt
python database.py           # Initialize DB
python sample_data.py       # Load test data
python main.py              # Run CLI app
```

## 📖 Learning Resources

- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [SQLite Docs](https://www.sqlite.org/docs.html)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)

## ✅ Checklist for Deployment

- [ ] Review ASSIGNMENT.md for accuracy
- [ ] Test starter_template/ code runs without errors
- [ ] Verify all solutions work correctly
- [ ] Run test suite: `pytest tests/`
- [ ] Update dates in assignment
- [ ] Add to website config.json
- [ ] Create submission instructions
- [ ] Set up grading rubric in your system

## 🤝 Support

**Common Issues:**
- Database not creating? Check permissions, see GETTING_STARTED.md
- Import errors? Install requirements.txt dependencies
- Tests failing? Review solutions/ for reference

See [FAQS.md](./FAQS.md) for more help.

---

**Assignment Created:** November 2024  
**Updated:** Ongoing
