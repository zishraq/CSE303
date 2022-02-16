nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = 0

for i in range(0, len(nums), 2):
    result += nums[i]

print('Sum of even-indexed elements: ', result)
