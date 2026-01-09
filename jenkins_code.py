import sys


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
    # Expected arguments:
    # script.py name department semester mark1 mark2 mark3
    if len(sys.argv) != 7:
        print("Usage: python jenkins_code.py <name> <department> <semester> <mark1> <mark2> <mark3>")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]

    try:
        marks = list(map(float, sys.argv[4:7]))
    except ValueError:
        print("Error: Marks must be numeric values")
        sys.exit(1)

    # Validate marks range
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100")
            sys.exit(1)

    average, grade = calculate_grade(marks)

    print("=== Student Result ===")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
