nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'

filtered_nums = [
    i for i in nums if [j for j in range(2, 10) if i % j == 0]
]

print(filtered_nums)
