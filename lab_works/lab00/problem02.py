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


courseA_credit = float(input('Enter credits of course A: '))
courseB_credit = float(input('Enter credits of course B: '))
courseC_credit = float(input('Enter credits of course C: '))

courseA_marks = float(input('Enter marks of course A: '))
courseB_marks = float(input('Enter marks of course B: '))
courseC_marks = float(input('Enter marks of course C: '))


total_grade_points = 0

total_grade_points += grade_points[get_grade(courseA_marks)] * courseA_credit
total_grade_points += grade_points[get_grade(courseB_marks)] * courseB_credit
total_grade_points += grade_points[get_grade(courseC_marks)] * courseC_credit

total_credits = courseA_credit + courseB_credit + courseC_credit

term_gpa = total_grade_points / total_credits

print('Term GPA', term_gpa)
