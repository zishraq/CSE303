my_string = str(input('Enter any string: '))


def palindrome_checker_2019_2_60_022(my_str: str):
    if my_str == my_str[::-1]:
        return True
    return False


if palindrome_checker_2019_2_60_022(my_string):
    print('The string is palindrome')

else:
    print('The string is not palindrome')
