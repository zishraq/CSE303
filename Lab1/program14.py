my_string = str(input('Enter any string: '))


def isPalindrome(my_str: str):
    if my_str == my_str[::-1]:
        return True
    return False


if isPalindrome(my_string):
    print('The string is palindrome')

else:
    print('The string is not palindrome')
