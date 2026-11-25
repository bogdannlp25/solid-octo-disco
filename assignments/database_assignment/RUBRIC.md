# Grading Rubric

## Total Points: 100

---

## 1. Database Schema Design (20 points)

### Full Points (20)
- [ ] Database schema is properly normalized (no data redundancy)
- [ ] All three tables created: Students, Projects, SkillsUsed
- [ ] Primary keys and foreign keys properly defined
- [ ] Relationships are correctly established (1-to-Many, etc.)
- [ ] Appropriate data types chosen for each column
- [ ] Column constraints (NOT NULL, UNIQUE, DEFAULT) are used correctly
- [ ] Schema supports the assignment requirements

### Partial Points (10-19)
- [ ] Schema is mostly correct but has minor normalization issues
- [ ] Most relationships are correct, 1-2 missing or incorrect
- [ ] Some data types are incorrect or suboptimal
- [ ] Most constraints are present

### Minimal Points (1-9)
- [ ] Schema exists but has significant issues
- [ ] Tables are missing or incomplete
- [ ] Relationships are poorly designed

### No Points (0)
- [ ] No schema provided or schema is non-functional

---

## 2. SQLAlchemy Models (20 points)

### Full Points (20)
- [ ] All three model classes defined (Student, Project, SkillUsed)
- [ ] Models correctly inherit from Base
- [ ] All columns properly defined with correct types
- [ ] Relationships are bidirectional where appropriate
- [ ] `back_populates` is used correctly
- [ ] Cascade rules are properly configured
- [ ] Models can be instantiated without errors
- [ ] `__repr__` methods for debugging (optional but appreciated)

### Partial Points (10-19)
- [ ] All models present but 1-2 have minor issues
- [ ] Most relationships work correctly
- [ ] Cascade rules may be missing or incomplete
- [ ] Models generally work with small bugs

### Minimal Points (1-9)
- [ ] Models exist but have significant issues
- [ ] Relationships don't work
- [ ] Models won't instantiate properly

### No Points (0)
- [ ] Models not provided or completely broken

---

## 3. CRUD Operations (20 points)

### Full Points (20)
- [ ] **CREATE:** `create_student()`, `create_project()`, `add_skill_to_project()` all work
- [ ] **READ:** At least 6 read functions implemented (get by ID, get all, filter operations)
- [ ] **UPDATE:** `update_student()` and `update_project()` work correctly
- [ ] **DELETE:** `delete_student()`, `delete_project()`, `delete_skill()` work
- [ ] All functions properly use SQLAlchemy sessions
- [ ] Functions handle edge cases (non-existent IDs, etc.)
- [ ] Database is properly committed after modifications
- [ ] No hardcoded database paths or connections

### Partial Points (10-19)
- [ ] Most CRUD operations implemented (1-2 missing)
- [ ] Functions work but may have minor bugs
- [ ] Session handling is mostly correct
- [ ] Some edge cases not handled

### Minimal Points (1-9)
- [ ] Only 1-2 CRUD operations work
- [ ] Significant bugs in multiple functions
- [ ] Session handling is incorrect

### No Points (0)
- [ ] CRUD operations not implemented or non-functional

---

## 4. Data Validation & Error Handling (10 points)

### Full Points (10)
- [ ] Database constraints prevent invalid data (unique emails, etc.)
- [ ] Error handling for common issues (duplicate emails, non-existent IDs)
- [ ] Input validation where appropriate
- [ ] Graceful failure messages (not crashes)
- [ ] Relationships enforced (can't create project without student_id)

### Partial Points (5-9)
- [ ] Some validation present, but not comprehensive
- [ ] Most constraints enforced
- [ ] Error handling works for main scenarios

### Minimal Points (1-4)
- [ ] Minimal validation
- [ ] Some invalid data can be inserted
- [ ] Limited error handling

### No Points (0)
- [ ] No validation or error handling

---

## 5. Code Quality & Organization (15 points)

### Full Points (15)
- [ ] Code is clean and well-organized
- [ ] Proper naming conventions (snake_case for functions/variables)
- [ ] Code is appropriately commented (not over-commented)
- [ ] No unnecessary complexity or duplication
- [ ] Follows Python style guidelines (PEP 8)
- [ ] All files properly named and organized

### Partial Points (10-14)
- [ ] Generally well-organized with minor issues
- [ ] Most code is clean and readable
- [ ] Some naming or style inconsistencies
- [ ] Minimal unnecessary complexity

### Minimal Points (5-9)
- [ ] Code works but is messy or hard to follow
- [ ] Poor naming or organization
- [ ] Multiple style violations

### No Points (0)
- [ ] Code is unreadable or incomprehensible

---

## 6. Testing & Verification (15 points)

### Full Points (15)
- [ ] Sample data loads successfully
- [ ] All CRUD operations verified with test data
- [ ] Queries return expected results
- [ ] All test cases pass (if provided)
- [ ] Application runs without errors
- [ ] Database can be reset and recreated
- [ ] Clear demonstration of working functionality

### Partial Points (10-14)
- [ ] Most features work correctly
- [ ] Minor test failures
- [ ] Sample data mostly loads
- [ ] Some edge cases not tested

### Minimal Points (5-9)
- [ ] Only basic testing done
- [ ] Some significant bugs found during testing
- [ ] Database has issues

### No Points (0)
- [ ] No testing or application doesn't run

---

## Grading Notes

### Deductions

- **-5 points** for each missing requirements file (requirements.txt)
- **-5 points** for missing or inadequate README
- **-10 points** for code that doesn't run (import errors, syntax errors)
- **-5 points** for hardcoded database paths instead of configuration
- **-3 points** per spelling/formatting error in documentation

### Bonuses

- **+5 points** for implementing optional FastAPI endpoints
- **+5 points** for comprehensive test suite (pytest)
- **+5 points** for advanced queries (get by language, category, etc.)
- **+5 points** for excellent documentation and comments

### Grade Scale

| Points | Grade |
|--------|-------|
| 90-100 | A     |
| 80-89  | B     |
| 70-79  | C     |
| 60-69  | D     |
| < 60   | F     |

---

## Student Submission Checklist

Print this and have students check off before submitting:

- [ ] All required files present (database.py, models.py, crud_operations.py, main.py)
- [ ] Code runs without errors
- [ ] All 3 tables created with correct schema
- [ ] All CRUD operations implemented and working
- [ ] Sample data loads successfully
- [ ] Application menu works (all options)
- [ ] Code is well-commented
- [ ] README.md explains how to run the code
- [ ] requirements.txt includes all dependencies
- [ ] No hardcoded paths or database URLs

**Total Files:**
- Python files: ___
- Database file (portfolio.db): Present ☐
- requirements.txt: Present ☐
- README.md: Present ☐

---

## Instructor Notes

### Time for Grading
Expect 10-15 minutes per submission:
- 2 min: Review code structure
- 3 min: Run application and test basic functions
- 3 min: Run test suite
- 2 min: Check documentation
- 2-3 min: Award points and write feedback

### Common Issues to Watch

1. **Foreign Key Errors** - Check if cascade rules are set
2. **Duplicate Data** - Look for unique constraints on emails
3. **Missing Relationships** - Verify back_populates is used
4. **Session Not Closing** - Check if sessions are properly managed
5. **Database Path Issues** - Ensure paths work on different systems

### Feedback Template

```
Grade: __/100

Strengths:
- [List 2-3 things they did well]

Areas to Improve:
- [List 2-3 things to work on]

Comments:
[Additional feedback, suggestions for extensions, etc.]
```

---

**Last Updated:** November 2024
