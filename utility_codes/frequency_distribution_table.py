import math

from tabulate import tabulate


def get_highest_limit(min_data, max_data, interval):
    lowermost_limit = min_data - (min_data % 10)
    uppermost_limit = lowermost_limit

    while uppermost_limit < max_data:
        uppermost_limit += interval

    return {
        'lower_limit': lowermost_limit,
        'upper_limit': uppermost_limit
    }


def generate_full_table_from_frequency_distribution(class_interval_list: list, frequency_list: list):
    frequency_distribution_table = {
        'Class Interval': [],
        'frequency (f)': [],
        'midpoint (x)': [],
        'fi * xi': [],
        'fi * (xi - x̄)^2': [],
        'CFi': [],
        'is_median_class': []
    }

    n = sum(frequency_list)
    frequency_distribution_table['Class Interval'] = class_interval_list
    frequency_distribution_table['frequency (f)'] = frequency_list

    if class_interval_list[0][1] == class_interval_list[1][0]:
        is_exclusive = False

    else:
        is_exclusive = True

    interval_range = class_interval_list[0][1] - class_interval_list[0][0]

    calculation_and_tabulation(frequency_distribution_table, interval_range, is_exclusive, n)


def generate_frequency_distribution_table(dataset: list, interval_range: int = 10, is_exclusive: bool = True):
    n = len(dataset)
    lowest_data = min(dataset)
    highest_data = max(dataset)

    get_limits = get_highest_limit(lowest_data, highest_data, interval_range)

    lowest_limit = get_limits['lower_limit']
    highest_limit = get_limits['upper_limit']

    frequency_distribution_table = {
        'Class Interval': [],
        'frequency (f)': [],
        'midpoint (x)': [],
        'fi * xi': [],
        'fi * (xi - x̄)^2': [],
        'CFi': [],
        'is_median_class': []
    }

    for interval in range(lowest_limit, highest_limit, interval_range):
        lower_limit = interval
        upper_limit = interval + interval_range - 1

        frequency_distribution_table['Class Interval'].append(
            [lower_limit, upper_limit if is_exclusive else upper_limit + 1])

        frequency_count = 0

        for data in dataset:
            if lower_limit <= data <= upper_limit:
                frequency_count += 1

        frequency_distribution_table['frequency (f)'].append(frequency_count)

    calculation_and_tabulation(frequency_distribution_table, interval_range, is_exclusive, n)


def calculation_and_tabulation(frequency_distribution_table, interval_range, is_exclusive, n):
    summation_fi_xi = 0

    for interval in range(len(frequency_distribution_table['Class Interval'])):
        lower_limit = frequency_distribution_table['Class Interval'][interval][0]
        upper_limit = frequency_distribution_table['Class Interval'][interval][1]

        midpoint = (lower_limit + upper_limit) / 2
        frequency_distribution_table['midpoint (x)'].append(midpoint)

        frequency_count = frequency_distribution_table['frequency (f)'][interval]

        fi_xi = frequency_count * midpoint
        frequency_distribution_table['fi * xi'].append(fi_xi)
        summation_fi_xi += fi_xi

    x_mean = summation_fi_xi / n

    cumulative_frequency = 0
    summation_fi_xi_xbar_squared = 0

    for interval in range(len(frequency_distribution_table['Class Interval'])):
        frequency = frequency_distribution_table['frequency (f)'][interval]
        x = frequency_distribution_table['midpoint (x)'][interval]
        cumulative_frequency += frequency
        fi_xi_xbar_squared = frequency * ((x - x_mean) ** 2)
        summation_fi_xi_xbar_squared += fi_xi_xbar_squared
        frequency_distribution_table['fi * (xi - x̄)^2'].append(fi_xi_xbar_squared)
        frequency_distribution_table['CFi'].append(cumulative_frequency)
        frequency_distribution_table['is_median_class'].append(False)

    # variance calculation and standard deviation
    variance = summation_fi_xi_xbar_squared / (n - 1)
    standard_deviation = math.sqrt(variance)

    # median calculation
    midvalue = n / 2
    median_class_index = 0

    for cfi in range(len(frequency_distribution_table['CFi'])):
        if midvalue <= frequency_distribution_table['CFi'][cfi]:
            median_class_index = cfi
            break

    frequency_distribution_table['is_median_class'][median_class_index] = True

    L = frequency_distribution_table['Class Interval'][median_class_index][0]
    B = frequency_distribution_table['CFi'][median_class_index - 1]
    G = frequency_distribution_table['frequency (f)'][median_class_index]
    w = interval_range + 1 if is_exclusive else interval_range

    median = L + ((midvalue - B) / G) * w

    print(tabulate(frequency_distribution_table, headers='keys', tablefmt='grid'))

    # Mean
    print('Mean calculations: ')
    print('Σ (fi * xi) =', summation_fi_xi)
    print('Mean =', x_mean)
    print()

    # Median
    print('Median calculations: ')
    print('L =', L)
    print('B =', B)
    print('G =', G)
    print('w =', w)
    print('Median =', median)
    print()

    print('Variance and Standard Deviation: ')
    print('Σ (fi * (xi - x̄)^2) =', summation_fi_xi_xbar_squared)
    print('Variance =', variance)
    print('Standard Deviation =', standard_deviation)
    print('-----------------------------------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    # dataset = []
    # generate_frequency_distribution_table(dataset)

    # generate_full_table_from_frequency_distribution(
    #     class_interval_list=[[20, 25], [25, 30], [30, 35], [35, 40], [40, 45]],
    #     frequency_list=[4, 10, 4, 4, 3]
    # )

    generate_full_table_from_frequency_distribution(
        class_interval_list=[[51, 55], [56, 60], [61, 65], [66, 70]],
        frequency_list=[2, 7, 8, 4]
    )
