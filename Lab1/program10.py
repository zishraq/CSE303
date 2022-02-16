nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def second_largest_number_2019_2_60_022(nums: list):
    nums.sort()
    return nums[-2]


print('Second largest element: ', second_largest_number_2019_2_60_022(nums))
