from math import pi


def get_circle_area(radius: float):
    return pi * (radius ** radius)


def get_circle_perimeter(radius: float):
    return 2 * pi * radius


rad = float(input('Enter radius: '))

print('Area of the circle is ', get_circle_area(rad))
print('Perimeter of the circle is ', get_circle_perimeter(rad))
