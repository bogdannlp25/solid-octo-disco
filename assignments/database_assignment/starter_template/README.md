# Starter Template - Student Portfolio Database

This is starter code to get you going. All files are provided as templates.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize database:**
   ```bash
   python database.py
   ```

3. **Load sample data:**
   ```bash
   python sample_data.py
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## Files

- `database.py` - Database connection and initialization
- `models.py` - SQLAlchemy ORM models
- `crud_operations.py` - CRUD functions
- `main.py` - CLI application
- `sample_data.py` - Sample data loader
- `requirements.txt` - Python dependencies

## Expected Output

When you run `python main.py`, you should see a menu:
```
==================================================
📚 Student Portfolio Manager
==================================================
1. Add a new student
2. View all students
3. Add a project
4. View student projects
5. View student statistics
6. Update a project grade
7. Exit
==================================================
```

## Troubleshooting

If `ModuleNotFoundError: No module named 'sqlalchemy'` appears:
```bash
pip install -r requirements.txt
```

If database errors occur:
```bash
rm data/portfolio.db
python database.py
python sample_data.py
```

---

See `GETTING_STARTED.md` in the parent folder for detailed walkthrough.
