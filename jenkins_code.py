import argparse
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
    parser = argparse.ArgumentParser(
        description="Student Grade Evaluation System"
    )

    parser.add_argument("--name", required=True, help="Student name")
    parser.add_argument("--department", required=True, help="Department")
    parser.add_argument("--semester", required=True, help="Semester")
    parser.add_argument(
        "--marks",
        required=True,
        nargs=3,
        type=float,
        help="Marks of three subjects"
    )

    args = parser.parse_args()

    # Validate marks range
    for mark in args.marks:
        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100")
            sys.exit(1)

    average, grade = calculate_grade(args.marks)

    print("=== Student Result ===")
    print(f"Name       : {args.name}")
    print(f"Department : {args.department}")
    print(f"Semester   : {args.semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
