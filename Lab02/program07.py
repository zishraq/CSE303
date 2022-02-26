nums = [i for i in range(1, 1001)]
string = 'Practice Problems to Drill List Comprehension in Your Head.'

nums_divisible_by_single_digit_except_1 = [
    i for i in nums if [j for j in range(2, 10) if i % j == 0]
]

print(nums_divisible_by_single_digit_except_1)
