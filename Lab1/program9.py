nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def largest_number_2019_2_60_022(nums: list):
    largest_num = nums[0]

    for i in nums:
        if i > largest_num:
            largest_num = i

    return largest_num


def smallest_number_2019_2_60_022(nums: list):
    smallest_num = nums[0]

    for i in nums:
        if i < smallest_num:
            smallest_num = i

    return smallest_num


print('Largest element: ', largest_number_2019_2_60_022(nums))
print('Smallest element: ', smallest_number_2019_2_60_022(nums))
