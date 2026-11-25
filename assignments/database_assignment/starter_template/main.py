"""
Main CLI application for the Student Portfolio Manager.

This provides an interactive menu for managing students and projects.
"""

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
