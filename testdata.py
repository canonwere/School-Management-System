if __name__ == "__main__":
    school = School()
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Add Grade")
        print("4. Mark Attendance")
        print("5. Save Data")
        print("6. Load Data")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade_level = input("Enter grade level: ")
            school.add_student(student_id, name, grade_level)

        elif choice == "2":
            student_id = input("Enter student ID: ")
            school.view_student(student_id)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            student = school.students.get(student_id)
            if student:
                student.add_grade(subject, grade)
                print(f"Added grade {grade} in {subject} for {student.name}")
            else:
                print("Student not found!")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter attendance status (Present/Absent): ")
            student = school.students.get(student_id)
            if student:
                student.mark_attendance(date, status)
                print(f"Marked {status} for {student.name} on {date}")
            else:
                print("Student not found!")

        elif choice == "5":
            school.save_data()

        elif choice == "6":
            school.load_data()

        elif choice == "0":
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")
