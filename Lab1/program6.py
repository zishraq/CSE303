def get_nth_fibonacci(n):
    if n == 0 or n == 1:
        return n

    return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)


N = int(input('Enter N: '))

print(get_nth_fibonacci(N))
