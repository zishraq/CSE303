nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'

words = string.split()


words_size = {
    word if '.' not in word else word.replace('.', ''): len(word) if '.' not in word else len(word) - 1 for word in words
}

print(words_size)
