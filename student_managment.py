"""
STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM
Data Organization Using Python Collections

Collections used:
1. Strings
2. Lists
3. Tuples
4. Sets
5. Dictionaries
"""

# ============================================================
# GLOBAL COLLECTIONS
# ============================================================

students = []

departments = set()
all_subjects = set()
clubs = set()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_number(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def find_student(roll_number):
    for student in students:

        if student["roll_number"][0].lower() == roll_number.lower():
            return student

    return None


def rebuild_sets():
    departments.clear()
    all_subjects.clear()
    clubs.clear()

    for student in students:
        departments.add(student["department"])
        all_subjects.update(student["subjects"])
        clubs.update(student["clubs"])


def calculate_student_average(student):
    if len(student["marks"]) == 0:
        return 0

    return sum(student["marks"]) / len(student["marks"])


# ============================================================
# DISPLAY STUDENT
# ============================================================

def display_student(student):

    print("\n")
    print("=" * 60)
    print("                    STUDENT PROFILE")
    print("=" * 60)

    print("Roll Number      :", student["roll_number"][0])
    print("Registration No. :", student["registration_number"][0])
    print("Name             :", student["name"])
    print("Department       :", student["department"])
    print("Date of Birth    :", student["dob"][0])

    print("\nAcademic Details")
    print("-" * 60)

    for i in range(len(student["subjects"])):

        subject = student["subjects"][i]
        mark = student["marks"][i]
        attendance = student["attendance"][i]

        print(
            f"{subject:<20}"
            f" Marks: {mark:>6.1f}"
            f"   Attendance: {attendance:>6.1f}%"
        )

    average = calculate_student_average(student)

    print(f"\nAverage Marks     : {average:.2f}")

    print("\nContact Information")
    print("-" * 60)

    print(
        "Email             :",
        student["contact_information"]["email"]
    )

    print(
        "Address           :",
        student["contact_information"]["address"]
    )

    if student["clubs"]:
        print(
            "Clubs             :",
            ", ".join(sorted(student["clubs"]))
        )
    else:
        print("Clubs             : None")

    print("=" * 60)


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    print("\n")
    print("=" * 60)
    print("                     ADD STUDENT")
    print("=" * 60)

    roll_number = get_non_empty("Enter Roll Number: ")

    if find_student(roll_number) is not None:
        print("\nA student with this roll number already exists.")
        return

    registration_number = get_non_empty(
        "Enter Registration Number: "
    )

    name = get_non_empty("Enter Student Name: ")

    department = get_non_empty("Enter Department: ")

    dob = get_non_empty(
        "Enter Date of Birth (DD-MM-YYYY): "
    )

    email = get_non_empty("Enter Email: ")

    address = get_non_empty("Enter Address: ")

    # Subjects - LIST
    while True:

        subjects_input = input(
            "Enter subjects separated by commas: "
        ).strip()

        subjects = [
            subject.strip()
            for subject in subjects_input.split(",")
            if subject.strip()
        ]

        if subjects:

            subjects = list(dict.fromkeys(subjects))
            break

        print("Please enter at least one subject.")

    # Marks - LIST
    marks = []

    for subject in subjects:

        mark = get_number(
            f"Enter marks for {subject} (0-100): ",
            0,
            100
        )

        marks.append(mark)

    # Attendance - LIST
    attendance = []

    for subject in subjects:

        value = get_number(
            f"Enter attendance for {subject} (0-100): ",
            0,
            100
        )

        attendance.append(value)

    # Clubs - SET
    club_input = input(
        "Enter clubs separated by commas (or press Enter for none): "
    ).strip()

    student_clubs = {
        club.strip()
        for club in club_input.split(",")
        if club.strip()
    }

    # TUPLES
    roll_number_tuple = (roll_number,)
    registration_number_tuple = (registration_number,)
    dob_tuple = (dob,)

    # DICTIONARY
    student = {

        "roll_number": roll_number_tuple,

        "registration_number": registration_number_tuple,

        "name": name,

        "department": department,

        "dob": dob_tuple,

        "subjects": subjects,

        "marks": marks,

        "attendance": attendance,

        "contact_information": {
            "email": email,
            "address": address
        },

        "clubs": student_clubs
    }

    # Add dictionary to LIST
    students.append(student)

    # Update SETS
    rebuild_sets()

    print("\nStudent record added successfully!")


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    print("\n")
    print("=" * 60)
    print("                   SEARCH STUDENT")
    print("=" * 60)

    roll_number = get_non_empty("Enter Roll Number: ")

    student = find_student(roll_number)

    if student is None:
        print("\nStudent not found.")
    else:
        display_student(student)


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    print("\n")
    print("=" * 60)
    print("                   UPDATE STUDENT")
    print("=" * 60)

    roll_number = get_non_empty("Enter Roll Number: ")

    student = find_student(roll_number)

    if student is None:
        print("\nStudent not found.")
        return

    print("\nPress Enter if you want to keep the existing value.")

    name = input(
        f"Name [{student['name']}]: "
    ).strip()

    department = input(
        f"Department [{student['department']}]: "
    ).strip()

    dob = input(
        f"Date of Birth [{student['dob'][0]}]: "
    ).strip()

    email = input(
        f"Email [{student['contact_information']['email']}]: "
    ).strip()

    address = input(
        f"Address [{student['contact_information']['address']}]: "
    ).strip()

    if name:
        student["name"] = name

    if department:
        student["department"] = department

    if dob:
        student["dob"] = (dob,)

    if email:
        student["contact_information"]["email"] = email

    if address:
        student["contact_information"]["address"] = address

    rebuild_sets()

    print("\nStudent record updated successfully!")


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    print("\n")
    print("=" * 60)
    print("                   DELETE STUDENT")
    print("=" * 60)

    roll_number = get_non_empty("Enter Roll Number: ")

    student = find_student(roll_number)

    if student is None:
        print("\nStudent not found.")
        return

    print(f"\nStudent found: {student['name']}")

    confirm = input(
        "Are you sure you want to delete this record? (y/n): "
    ).strip().lower()

    if confirm == "y":

        students.remove(student)
        rebuild_sets()

        print("\nStudent record deleted successfully!")

    else:
        print("\nDelete operation cancelled.")


# ============================================================
# DISPLAY ALL STUDENTS
# ============================================================

def display_all_students():

    print("\n")
    print("=" * 60)
    print("                 ALL STUDENT RECORDS")
    print("=" * 60)

    if len(students) == 0:

        print("\nNo student records available.")
        return

    for student in students:
        display_student(student)


# ============================================================
# CALCULATE AVERAGE
# ============================================================

def calculate_average():

    print("\n")
    print("=" * 60)
    print("                  CALCULATE AVERAGE")
    print("=" * 60)

    roll_number = get_non_empty("Enter Roll Number: ")

    student = find_student(roll_number)

    if student is None:

        print("\nStudent not found.")
        return

    average = calculate_student_average(student)

    print("\nStudent       :", student["name"])
    print("Average Marks :", f"{average:.2f}")


# ============================================================
# FIND HIGHEST SCORER
# ============================================================

def highest_scorer():

    print("\n")
    print("=" * 60)
    print("                    HIGHEST SCORER")
    print("=" * 60)

    if len(students) == 0:

        print("\nNo student records available.")
        return

    highest_student = max(
        students,
        key=calculate_student_average
    )

    highest_average = calculate_student_average(
        highest_student
    )

    print("\nHighest Scorer")
    print("-" * 60)

    print(
        "Name          :",
        highest_student["name"]
    )

    print(
        "Roll Number   :",
        highest_student["roll_number"][0]
    )

    print(
        "Department    :",
        highest_student["department"]
    )

    print(
        "Average Marks :",
        f"{highest_average:.2f}"
    )


# ============================================================
# STUDENTS BY DEPARTMENT
# ============================================================

def students_by_department():

    print("\n")
    print("=" * 60)
    print("                STUDENTS BY DEPARTMENT")
    print("=" * 60)

    if len(students) == 0:

        print("\nNo student records available.")
        return

    department = get_non_empty("Enter Department: ")

    found = False

    print("\nMatching Students")
    print("-" * 60)

    for student in students:

        if student["department"].lower() == department.lower():

            print(
                "Roll Number:",
                student["roll_number"][0],
                "| Name:",
                student["name"]
            )

            found = True

    if not found:

        print("No students found in this department.")


# ============================================================
# COUNT STUDENTS
# ============================================================

def count_students():

    print("\n")
    print("=" * 60)
    print("                    STUDENT COUNT")
    print("=" * 60)

    print("\nTotal Students:", len(students))


# ============================================================
# DISPLAY COLLECTIONS
# ============================================================

def display_collections():

    print("\n")
    print("=" * 60)
    print("                COLLECTION INFORMATION")
    print("=" * 60)

    print("\nUnique Departments:")

    if departments:

        for department in sorted(departments):
            print("-", department)

    else:
        print("None")

    print("\nUnique Subjects:")

    if all_subjects:

        for subject in sorted(all_subjects):
            print("-", subject)

    else:
        print("None")

    print("\nUnique Student Clubs:")

    if clubs:

        for club in sorted(clubs):
            print("-", club)

    else:
        print("None")


# ============================================================
# REPORT MENU
# ============================================================

def generate_reports():

    while True:

        print("\n")
        print("=" * 60)
        print("                       REPORTS")
        print("=" * 60)

        print("1. Highest Scorer")
        print("2. Students by Department")
        print("3. Calculate Average Marks")
        print("4. Student Count")
        print("5. Collection Information")
        print("0. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            highest_scorer()

        elif choice == "2":
            students_by_department()

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            count_students()

        elif choice == "5":
            display_collections()

        elif choice == "0":
            break

        else:
            print("\nInvalid choice. Please try again.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("     STUDENT RECORD & ACADEMIC MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1.  Add Student")
        print("2.  Search Student")
        print("3.  Update Student")
        print("4.  Delete Student")
        print("5.  Display All Students")
        print("6.  Calculate Average Marks")
        print("7.  Find Highest Scorer")
        print("8.  List Students by Department")
        print("9.  Count Students")
        print("10. Generate Reports")
        print("0.  Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_all_students()

        elif choice == "6":
            calculate_average()

        elif choice == "7":
            highest_scorer()

        elif choice == "8":
            students_by_department()

        elif choice == "9":
            count_students()

        elif choice == "10":
            generate_reports()

        elif choice == "0":

            print("\nThank you for using the system!")
            print("Program ended.")

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 0 to 10."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()