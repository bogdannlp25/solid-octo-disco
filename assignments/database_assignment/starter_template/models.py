"""
SQLAlchemy ORM models for the portfolio database.

This module defines the structure of our database tables as Python classes.
"""

from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Student(Base):
    """Student model - represents a student in the portfolio system"""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    grade = Column(Integer)  # Grade level: 9-12
    bio = Column(Text)
    joined_date = Column(String, default=str(datetime.now()))
    
    # Relationship: one student has many projects
    projects = relationship(
        "Project",
        back_populates="student",
        cascade="all, delete-orphan"
    )
    
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
    skills = relationship(
        "SkillUsed",
        back_populates="project",
        cascade="all, delete-orphan"
    )
    
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
