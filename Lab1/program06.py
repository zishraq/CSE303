def get_nth_fibonacci(n):
    num1 = 0
    num2 = 1

    if n == 0:
        return 0

    elif n == 1:
        return num2

    else:
        for i in range(1, n):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num2


N = int(input('Enter N: '))

print(get_nth_fibonacci(N))
