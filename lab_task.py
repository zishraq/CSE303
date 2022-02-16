student_marks = [(100, 90, 80), (70, 80, 90), (85, 75, 65), (100, 90, 95)]


def custom_sort(value):
    return sum(list(value))


student_marks.sort(key=custom_sort, reverse=True)

print(student_marks)
