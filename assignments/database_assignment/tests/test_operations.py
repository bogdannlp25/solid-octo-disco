"""
Test suite for the Student Portfolio Database Manager.

Run with: pytest test_operations.py
"""

import pytest
import os
import sys

# Add parent directory to path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, Base, engine, init_db
from crud_operations import *
from models import Student, Project, SkillUsed


@pytest.fixture
def db():
    """Create a fresh database for each test"""
    # Create tables
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    # Clean up after test
    Base.metadata.drop_all(bind=engine)


class TestStudentOperations:
    """Test Student CRUD operations"""
    
    def test_create_student(self, db):
        """Test creating a student"""
        student = create_student(db, "John Doe", "john@school.edu", 11, "Bio")
        assert student.id is not None
        assert student.name == "John Doe"
        assert student.email == "john@school.edu"
    
    def test_get_student_by_id(self, db):
        """Test retrieving student by ID"""
        student = create_student(db, "Jane Doe", "jane@school.edu", 10)
        found = get_student_by_id(db, student.id)
        assert found is not None
        assert found.name == "Jane Doe"
    
    def test_get_student_by_email(self, db):
        """Test retrieving student by email"""
        create_student(db, "Bob Smith", "bob@school.edu", 11)
        found = get_student_by_email(db, "bob@school.edu")
        assert found is not None
        assert found.name == "Bob Smith"
    
    def test_get_all_students(self, db):
        """Test retrieving all students"""
        create_student(db, "Student 1", "s1@school.edu", 9)
        create_student(db, "Student 2", "s2@school.edu", 10)
        create_student(db, "Student 3", "s3@school.edu", 11)
        
        students = get_all_students(db)
        assert len(students) == 3
    
    def test_update_student(self, db):
        """Test updating student information"""
        student = create_student(db, "Original Name", "orig@school.edu", 10)
        updated = update_student(db, student.id, name="New Name", grade=12)
        assert updated.name == "New Name"
        assert updated.grade == 12
    
    def test_delete_student(self, db):
        """Test deleting a student"""
        student = create_student(db, "To Delete", "delete@school.edu", 11)
        success = delete_student(db, student.id)
        assert success is True
        found = get_student_by_id(db, student.id)
        assert found is None
    
    def test_unique_email_constraint(self, db):
        """Test that email must be unique"""
        create_student(db, "Student A", "same@school.edu", 11)
        with pytest.raises(Exception):  # Should raise integrity error
            create_student(db, "Student B", "same@school.edu", 11)
            db.commit()


class TestProjectOperations:
    """Test Project CRUD operations"""
    
    def test_create_project(self, db):
        """Test creating a project"""
        student = create_student(db, "John Doe", "john@school.edu", 11)
        project = create_project(
            db,
            student_id=student.id,
            title="Test Project",
            language="Python",
            category="Game"
        )
        assert project.id is not None
        assert project.title == "Test Project"
    
    def test_get_project_by_id(self, db):
        """Test retrieving project by ID"""
        student = create_student(db, "Jane Doe", "jane@school.edu", 10)
        project = create_project(db, student.id, "My Project")
        found = get_project_by_id(db, project.id)
        assert found is not None
        assert found.title == "My Project"
    
    def test_get_student_projects(self, db):
        """Test retrieving all projects for a student"""
        student = create_student(db, "Bob Smith", "bob@school.edu", 11)
        create_project(db, student.id, "Project 1")
        create_project(db, student.id, "Project 2")
        create_project(db, student.id, "Project 3")
        
        projects = get_student_projects(db, student.id)
        assert len(projects) == 3
    
    def test_get_projects_by_language(self, db):
        """Test filtering projects by language"""
        student = create_student(db, "Alice", "alice@school.edu", 11)
        create_project(db, student.id, "Python Game", language="Python")
        create_project(db, student.id, "JavaScript App", language="JavaScript")
        create_project(db, student.id, "Python Web", language="Python")
        
        python_projects = get_projects_by_language(db, "Python")
        assert len(python_projects) == 2
    
    def test_get_projects_by_category(self, db):
        """Test filtering projects by category"""
        student = create_student(db, "Bob", "bob@school.edu", 10)
        create_project(db, student.id, "Game 1", category="Game")
        create_project(db, student.id, "Game 2", category="Game")
        create_project(db, student.id, "Web App", category="Web App")
        
        games = get_projects_by_category(db, "Game")
        assert len(games) == 2
    
    def test_update_project(self, db):
        """Test updating project information"""
        student = create_student(db, "Student", "student@school.edu", 11)
        project = create_project(db, student.id, "Original Title")
        updated = update_project(db, project.id, title="Updated Title", grade_received=95)
        assert updated.title == "Updated Title"
        assert updated.grade_received == 95
    
    def test_delete_project(self, db):
        """Test deleting a project"""
        student = create_student(db, "Student", "student@school.edu", 11)
        project = create_project(db, student.id, "To Delete")
        success = delete_project(db, project.id)
        assert success is True
        found = get_project_by_id(db, project.id)
        assert found is None


class TestSkillOperations:
    """Test Skill CRUD operations"""
    
    def test_add_skill_to_project(self, db):
        """Test adding a skill to a project"""
        student = create_student(db, "Student", "student@school.edu", 11)
        project = create_project(db, student.id, "Project")
        skill = add_skill_to_project(db, project.id, "OOP")
        assert skill.id is not None
        assert skill.skill_name == "OOP"
    
    def test_get_project_skills(self, db):
        """Test retrieving all skills for a project"""
        student = create_student(db, "Student", "student@school.edu", 11)
        project = create_project(db, student.id, "Project")
        add_skill_to_project(db, project.id, "OOP")
        add_skill_to_project(db, project.id, "Inheritance")
        add_skill_to_project(db, project.id, "Polymorphism")
        
        skills = get_project_skills(db, project.id)
        assert len(skills) == 3
    
    def test_delete_skill(self, db):
        """Test deleting a skill"""
        student = create_student(db, "Student", "student@school.edu", 11)
        project = create_project(db, student.id, "Project")
        skill = add_skill_to_project(db, project.id, "To Delete")
        success = delete_skill(db, skill.id)
        assert success is True


class TestRelationships:
    """Test model relationships"""
    
    def test_student_has_projects(self, db):
        """Test that student can access their projects through relationship"""
        student = create_student(db, "John", "john@school.edu", 11)
        create_project(db, student.id, "Project 1")
        create_project(db, student.id, "Project 2")
        
        # Retrieve and check relationship
        found_student = get_student_by_id(db, student.id)
        assert len(found_student.projects) == 2
    
    def test_project_has_skills(self, db):
        """Test that project can access skills through relationship"""
        student = create_student(db, "Jane", "jane@school.edu", 11)
        project = create_project(db, student.id, "Project")
        add_skill_to_project(db, project.id, "Skill 1")
        add_skill_to_project(db, project.id, "Skill 2")
        
        # Retrieve and check relationship
        found_project = get_project_by_id(db, project.id)
        assert len(found_project.skills) == 2
    
    def test_cascade_delete_projects(self, db):
        """Test that deleting student cascades to projects"""
        student = create_student(db, "To Delete", "delete@school.edu", 11)
        project = create_project(db, student.id, "Project")
        
        # Delete student
        delete_student(db, student.id)
        
        # Project should also be deleted
        found_project = get_project_by_id(db, project.id)
        assert found_project is None


class TestAnalytics:
    """Test analytics functions"""
    
    def test_get_student_stats(self, db):
        """Test calculating student statistics"""
        student = create_student(db, "John", "john@school.edu", 11)
        create_project(db, student.id, "Project 1", language="Python", category="Game", grade=90)
        create_project(db, student.id, "Project 2", language="Python", category="Web", grade=95)
        
        stats = get_student_stats(db, student.id)
        assert stats['total_projects'] == 2
        assert stats['avg_grade'] == 92.5
        assert "Python" in stats['languages_used']
        assert "Game" in stats['categories']
    
    def test_student_stats_no_projects(self, db):
        """Test stats for student with no projects"""
        student = create_student(db, "Empty", "empty@school.edu", 11)
        stats = get_student_stats(db, student.id)
        assert stats['total_projects'] == 0
        assert stats['avg_grade'] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
