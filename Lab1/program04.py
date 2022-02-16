def calculate_series(n: int) -> int:
    result = 0

    for i in range(1, n + 1):
        result += (i ** 2)

    return result


N = int(input('Enter N: '))

print('Series result = ', calculate_series(N))
