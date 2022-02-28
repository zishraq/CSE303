nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'


vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    string = string.replace(vowel, '')

print(string)
