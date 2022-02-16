myString = str(input('Enter any string: '))
n = int(input('Enter n (characters to be removed): '))

if n >= len(myString):
    print('n should be less than the length of string.')

else:
    newString = ''

    for i in range(n, len(myString)):
        newString += myString[i]

    print('String after removing n characters: ', newString)
