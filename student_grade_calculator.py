"""
Student Grade Calculator Program
Manages student records with test scores and calculates grades
Data structure: Using Student class (Option B)
"""

import os
from typing import List, Optional


class Student:
    """Represents a student with name, ID, test scores, average, and grade."""
    
    def __init__(self, name: str, student_id: str, test1: float, test2: float, test3: float):
        """Initialize a student with name, ID, and three test scores."""
        self.name = name
        self.student_id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
    
    def calculate_average(self) -> float:
        """Calculate and return the average of the three test scores."""
        return (self.test1 + self.test2 + self.test3) / 3
    
    def calculate_grade(self) -> str:
        """Calculate and return the letter grade based on average."""
        self.average = self.calculate_average()
        
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self) -> str:
        """Return a string representation in pipe-delimited format."""
        return f"{self.name}|{self.student_id}|{self.test1:.2f}|{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}"
    
    @classmethod
    def from_string(cls, line: str) -> 'Student':
        """Create a Student instance from a pipe-delimited string."""
        parts = line.strip().split('|')
        name, student_id, test1, test2, test3 = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
        return cls(name, student_id, test1, test2, test3)


# ============ FILE OPERATIONS ============

def load_students(filename: str = "student_grades.txt") -> List[Student]:
    """Load student records from a file. Returns empty list if file doesn't exist."""
    students = []
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        students.append(Student.from_string(line))
            print(f"✓ Loaded {len(students)} student(s) from '{filename}'")
        else:
            print(f"ℹ No existing file found. Starting with empty records.")
    except Exception as e:
        print(f"✗ Error loading file: {e}")
    
    return students


def save_students(students: List[Student], filename: str = "student_grades.txt") -> bool:
    """Save all student records to a file. Returns True if successful."""
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(str(student) + '\n')
        print(f"✓ Saved {len(students)} student(s) to '{filename}'")
        return True
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return False


# ============ INPUT VALIDATION ============

def get_valid_float(prompt: str, min_val: float = 0, max_val: float = 100) -> float:
    """Get a valid float input within specified range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"✗ Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("✗ Invalid input. Please enter a valid number.")


def get_valid_string(prompt: str) -> str:
    """Get a non-empty string input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("✗ Input cannot be empty.")


# ============ STUDENT MANAGEMENT ============

def add_student(students: List[Student]) -> None:
    """Add a new student to the list."""
    print("\n--- Add New Student ---")
    
    name = get_valid_string("Enter student name: ")
    student_id = get_valid_string("Enter student ID: ")
    
    test1 = get_valid_float("Enter Test 1 score (0-100): ")
    test2 = get_valid_float("Enter Test 2 score (0-100): ")
    test3 = get_valid_float("Enter Test 3 score (0-100): ")
    
    student = Student(name, student_id, test1, test2, test3)
    students.append(student)
    
    print(f"\n✓ Student '{name}' added successfully!")
    print(f"  Average: {student.average:.2f} | Grade: {student.grade}")


def display_all_students(students: List[Student]) -> None:
    """Display all students in a formatted table."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    print("\n" + "=" * 90)
    print(f"{'Name':<20} {'Student ID':<15} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<5}")
    print("=" * 90)
    
    for student in students:
        print(f"{student.name:<20} {student.student_id:<15} {student.test1:<10.2f} {student.test2:<10.2f} {student.test3:<10.2f} {student.average:<10.2f} {student.grade:<5}")
    
    print("=" * 90)


def search_student(students: List[Student]) -> None:
    """Search for a student by name (case-insensitive)."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    search_name = get_valid_string("\nEnter student name to search: ").lower()
    
    results = [s for s in students if search_name in s.name.lower()]
    
    if results:
        print(f"\n--- Search Results for '{search_name}' ---")
        print(f"{'Name':<20} {'Student ID':<15} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<5}")
        print("-" * 90)
        for student in results:
            print(f"{student.name:<20} {student.student_id:<15} {student.test1:<10.2f} {student.test2:<10.2f} {student.test3:<10.2f} {student.average:<10.2f} {student.grade:<5}")
    else:
        print(f"\n✗ No student found with name '{search_name}'")


def calculate_class_statistics(students: List[Student]) -> None:
    """Calculate and display class statistics."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    averages = [s.average for s in students]
    
    highest_student = max(students, key=lambda s: s.average)
    lowest_student = min(students, key=lambda s: s.average)
    class_average = sum(averages) / len(averages)
    
    print("\n" + "=" * 50)
    print("CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Average: {highest_student.average:.2f} ({highest_student.name})")
    print(f"Lowest Average: {lowest_student.average:.2f} ({lowest_student.name})")
    print("=" * 50)


# ============ MENU SYSTEM ============

def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print("1. Add new student")
    print("2. Display all students")
    print("3. Search student by name")
    print("4. View class statistics")
    print("5. Save and exit (ESC)")
    print("=" * 50)


def main() -> None:
    """Main program loop."""
    students = load_students()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5) or press ESC to exit: ").strip().lower()
        
        if choice in ('5', 'esc', '\x1b'):
            print("\n--- Saving and Exiting ---")
            save_students(students)
            print("✓ Goodbye!")
            break
        elif choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            calculate_class_statistics(students)
        else:
            print("✗ Invalid choice. Please enter 1-5 or ESC to exit.")


if __name__ == "__main__":
    main()
