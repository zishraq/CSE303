def prime_find_2019_2_60_022(num : int) -> bool:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False

    return True


N = int(input('Enter N: '))

if prime_find_2019_2_60_022(N):
    print('The number is a Prime number')

else:
    print('The number is not a Prime number')
