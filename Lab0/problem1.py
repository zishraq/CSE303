a = float(input('First side, a = '))
b = float(input('Second side, b = '))
c = float(input('Third side, c = '))


if a + b > c and c + b > a and a + c > b:
    s = (a + b + c) / 2
    print((s * (s - a) * (s - b) * (s - c)) ** 0.5)

else:
    print('Invalid sizes. Valid triangle condition: Sum of two sides should be greater than the third')
