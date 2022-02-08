grade_points = {
    'A': 4.0,
    'B': 3.5,
    'C': 3.0,
    'D': 2.5,
    'F': 0.0
}


def get_grade(marks: float):
    if marks <= 59:
        return 'F'

    if 60 <= marks <= 69:
        return 'D'

    if 70 <= marks <= 84:
        return 'C'

    if 85 <= marks <= 94:
        return 'B'

    if 95 <= marks <= 100:
        return 'A'


course1_credit = float(input('Enter credits of course A: '))
course2_credit = float(input('Enter credits of course B: '))
course3_credit = float(input('Enter credits of course C: '))

course1_marks = float(input('Enter marks of course A: '))
course2_marks = float(input('Enter marks of course B: '))
course3_marks = float(input('Enter marks of course C: '))


total_grade_points = 0

total_grade_points += grade_points[get_grade(course1_marks)] * course1_credit
total_grade_points += grade_points[get_grade(course2_marks)] * course2_credit
total_grade_points += grade_points[get_grade(course3_marks)] * course3_credit

total_credits = course1_credit + course2_credit + course3_credit

term_gpa = total_grade_points / total_credits

print('Term GPA', term_gpa)
