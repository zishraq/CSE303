nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'


words = string.split(' ')

for word in words:
    if len(word) < 5:
        print(word)
