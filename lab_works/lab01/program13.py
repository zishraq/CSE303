myString = str(input('Enter any string: '))
search_term = 'CSE303'
count = 0

for i in range(len(myString) - len(search_term) + 1):
    if myString[i: i + len(search_term)] == search_term:
        count += 1

print('CSE303 is in the string', count, 'times')
