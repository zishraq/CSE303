def get_nth_fibonacci(n):
    if n == 0 or n == 1:
        return n

    num1 = 0
    num2 = 1

    for i in range(1, n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    return num2


N = int(input('Enter N: '))

print(get_nth_fibonacci(N))
