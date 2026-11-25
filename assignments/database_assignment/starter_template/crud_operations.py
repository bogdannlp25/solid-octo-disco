"""
CRUD operations for the portfolio database.

This module contains all Create, Read, Update, Delete functions.
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
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


def get_all_students(db: Session) -> list:
    """Get all students"""
    return db.query(Student).all()


def get_project_by_id(db: Session, project_id: int) -> Project:
    """Get a project by ID"""
    return db.query(Project).filter(Project.id == project_id).first()


def get_student_projects(db: Session, student_id: int) -> list:
    """Get all projects for a specific student"""
    return db.query(Project).filter(Project.student_id == student_id).all()


def get_projects_by_language(db: Session, language: str) -> list:
    """Get all projects written in a specific language"""
    return db.query(Project).filter(Project.programming_language == language).all()


def get_projects_by_category(db: Session, category: str) -> list:
    """Get all projects in a specific category"""
    return db.query(Project).filter(Project.category == category).all()


def get_project_skills(db: Session, project_id: int) -> list:
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
    """Delete a student (and all their projects via cascade)"""
    student = get_student_by_id(db, student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False


def delete_project(db: Session, project_id: int) -> bool:
    """Delete a project (and all associated skills via cascade)"""
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
    
    # Calculate average grade
    grades = [p.grade_received for p in projects if p.grade_received]
    avg_grade = sum(grades) / len(grades) if grades else 0
    
    return {
        "student_name": student.name,
        "total_projects": len(projects),
        "avg_grade": avg_grade,
        "languages_used": list(set(p.programming_language for p in projects if p.programming_language)),
        "categories": list(set(p.category for p in projects if p.category))
    }
