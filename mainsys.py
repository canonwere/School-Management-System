import json

# Student Class
class Student:
    def __init__(self, student_id, name, grade_level):
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level
        self.grades = {}
        self.attendance = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def mark_attendance(self, date, status):
        self.attendance.append({"date": date, "status": status})

# School Management Class
class School:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, grade_level):
        if student_id in self.students:
            print("Student ID already exists!")
        else:
            student = Student(student_id, name, grade_level)
            self.students[student_id] = student
            print(f"Added student: {name}")

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Student Name: {student.name}")
            print(f"Grade Level: {student.grade_level}")
            print(f"Grades: {student.grades}")
            print(f"Attendance: {student.attendance}")
        else:
            print("Student not found!")

    def save_data(self, filename="school_data.json"):
        data = {student_id: student.__dict__ for student_id, student in self.students.items()}
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully!")

    def load_data(self, filename="school_data.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            for student_id, student_data in data.items():
                student = Student(student_data['student_id'], student_data['name'], student_data['grade_level'])
                student.grades = student_data['grades']
                student.attendance = student_data['attendance']
                self.students[student_id] = student
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No saved data found.")
