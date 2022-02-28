nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'


vowels = ['a', 'e', 'i', 'o', 'u']

new_string = string

for vowel in vowels:
    new_string = new_string.replace(vowel, '')

print(new_string)
