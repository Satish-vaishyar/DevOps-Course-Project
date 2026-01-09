def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if 90 <= average <= 100:
        grade = "S"
    elif 80 <= average < 90:
        grade = "A"
    elif 65 <= average < 80:
        grade = "B"
    elif 50 <= average < 65:
        grade = "C"
    elif 40 <= average < 50:
        grade = "D"
    else:
        grade = "F"

    return average, grade


def main():
    print("=== Student Grade Evaluation System ===")

    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    average, grade = calculate_grade(marks)

    print("\n--- Student Result ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
