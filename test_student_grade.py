from student_grade import calculate_grade

def test_grade_s():
    avg, grade = calculate_grade([95, 92, 93])
    assert grade == "S"

def test_grade_a():
    avg, grade = calculate_grade([85, 82, 88])
    assert grade == "A"

def test_grade_f():
    avg, grade = calculate_grade([30, 35, 38])
    assert grade == "F"
