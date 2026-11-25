"""
Sample data loader for the Student Portfolio Manager.

This script creates sample data for testing and demonstration.
"""

from database import SessionLocal, init_db
from crud_operations import *

def load_sample_data():
    """Load sample data into the database"""
    db = SessionLocal()
    
    # Clear existing data
    db.query(Student).delete()
    db.query(Project).delete()
    db.query(SkillUsed).delete()
    
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
