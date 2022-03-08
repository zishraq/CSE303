import math
import copy

from tabulate import tabulate
from extract_data import get_extracted_data

frequency_distribution_table_template = {
    'Class Interval': [],
    'frequency (f)': [],
    'midpoint (x)': [],
    'fi * xi': [],
    'fi * (xi - x̄)^2': [],
    'fi * (xi - x̄)^3': [],
    'fi * (xi - x̄)^4': [],
    'CFi': [],
    'is_median_class': []
}


def get_highest_limit(min_data, max_data, interval):
    lowermost_limit = min_data - (min_data % 10)
    uppermost_limit = lowermost_limit

    while uppermost_limit < max_data:
        uppermost_limit += interval

    return {
        'lower_limit': lowermost_limit,
        'upper_limit': uppermost_limit
    }


def get_frequency_list(lowest_limit, highest_limit, interval_range, dataset):
    frequency_list = []

    for interval in range(lowest_limit, highest_limit, interval_range):
        lower_limit = interval
        upper_limit = interval + interval_range - 1

        frequency_count = 0

        for data in dataset:
            if lower_limit <= data <= upper_limit:
                frequency_count += 1

        frequency_list.append(frequency_count)

    return frequency_list


def complete_table_from_frequency_distribution(class_interval_list: list, frequency_list: list):
    frequency_distribution_table = copy.deepcopy(frequency_distribution_table_template)
    n = sum(frequency_list)
    frequency_distribution_table['Class Interval'] = class_interval_list
    frequency_distribution_table['frequency (f)'] = frequency_list

    if class_interval_list[0][1] == class_interval_list[1][0]:
        is_exclusive = False

    else:
        is_exclusive = True

    interval_range = class_interval_list[0][1] - class_interval_list[0][0]

    calculation_and_tabulation(
        frequency_distribution_table=frequency_distribution_table,
        interval_range=interval_range,
        is_exclusive=is_exclusive,
        n=n
    )


def complete_table_from_class_interval(class_interval_list, dataset):
    frequency_distribution_table = copy.deepcopy(frequency_distribution_table_template)

    n = len(dataset)
    frequency_distribution_table['Class Interval'] = class_interval_list

    if class_interval_list[0][1] == class_interval_list[1][0]:
        is_exclusive = False

    else:
        is_exclusive = True

    interval_range = class_interval_list[0][1] - class_interval_list[0][0]

    frequency_distribution_table['frequency (f)'] = get_frequency_list(
        lowest_limit=class_interval_list[0][0],
        highest_limit=class_interval_list[-1][-1],
        interval_range=interval_range,
        dataset=dataset
    )

    calculation_and_tabulation(
        frequency_distribution_table=frequency_distribution_table,
        interval_range=interval_range,
        is_exclusive=is_exclusive,
        n=n
    )


def generate_frequency_distribution_table(dataset: list, interval_range: int = 10, is_exclusive: bool = True):
    n = len(dataset)
    lowest_data = min(dataset)
    highest_data = max(dataset)

    get_limits = get_highest_limit(lowest_data, highest_data, interval_range)

    lowest_limit = get_limits['lower_limit']
    highest_limit = get_limits['upper_limit']

    frequency_distribution_table = copy.deepcopy(frequency_distribution_table_template)

    for interval in range(lowest_limit, highest_limit, interval_range):
        lower_limit = interval
        upper_limit = interval + interval_range - 1

        frequency_distribution_table['Class Interval'].append([lower_limit, upper_limit if is_exclusive else upper_limit + 1])

    frequency_distribution_table['frequency (f)'] = get_frequency_list(
        lowest_limit=lowest_limit,
        highest_limit=highest_limit,
        interval_range=interval_range,
        dataset=dataset
    )

    calculation_and_tabulation(
        frequency_distribution_table=frequency_distribution_table,
        interval_range=interval_range,
        is_exclusive=is_exclusive,
        n=n
    )


def calculation_and_tabulation(frequency_distribution_table, interval_range, is_exclusive, n):
    for interval in range(len(frequency_distribution_table['Class Interval'])):
        lower_limit = frequency_distribution_table['Class Interval'][interval][0]
        upper_limit = frequency_distribution_table['Class Interval'][interval][1]

        midpoint = (lower_limit + upper_limit) / 2
        frequency_distribution_table['midpoint (x)'].append(midpoint)

        frequency_count = frequency_distribution_table['frequency (f)'][interval]

        fi_xi = frequency_count * midpoint
        frequency_distribution_table['fi * xi'].append(fi_xi)

    summation_fi_xi = sum(frequency_distribution_table['fi * xi'])
    x_mean = summation_fi_xi / n

    cumulative_frequency = 0

    for interval in range(len(frequency_distribution_table['Class Interval'])):
        frequency = frequency_distribution_table['frequency (f)'][interval]
        x = frequency_distribution_table['midpoint (x)'][interval]
        cumulative_frequency += frequency

        fi_xi_xbar_squared = frequency * ((x - x_mean) ** 2)
        fi_xi_xbar_cubed = frequency * ((x - x_mean) ** 3)
        fi_xi_xbar_to_4 = frequency * ((x - x_mean) ** 4)

        frequency_distribution_table['fi * (xi - x̄)^2'].append(fi_xi_xbar_squared)
        frequency_distribution_table['fi * (xi - x̄)^3'].append(fi_xi_xbar_cubed)
        frequency_distribution_table['fi * (xi - x̄)^4'].append(fi_xi_xbar_to_4)
        frequency_distribution_table['CFi'].append(cumulative_frequency)
        frequency_distribution_table['is_median_class'].append(False)

    # variance calculation and standard deviation
    summation_fi_xi_xbar_squared = sum(frequency_distribution_table['fi * (xi - x̄)^2'])
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

    # skewness calculation
    summation_fi_xi_xbar_cubed = sum(frequency_distribution_table['fi * (xi - x̄)^3'])
    skewness = summation_fi_xi_xbar_cubed / ((n - 1) * (standard_deviation ** 3))

    # kurtosis calculation
    summation_fi_xi_xbar_to_4 = sum(frequency_distribution_table['fi * (xi - x̄)^4'])
    kurtosis = summation_fi_xi_xbar_to_4 / ((n - 1) * (standard_deviation ** 4))

    frequency_distribution_table['Class Interval'].append('-')
    frequency_distribution_table['frequency (f)'].append(f'= {n}')
    frequency_distribution_table['midpoint (x)'].append('-')
    frequency_distribution_table['fi * xi'].append(f'= {summation_fi_xi}')
    frequency_distribution_table['fi * (xi - x̄)^2'].append(f'= {summation_fi_xi_xbar_squared}')
    frequency_distribution_table['fi * (xi - x̄)^3'].append(f'= {summation_fi_xi_xbar_cubed}')
    frequency_distribution_table['fi * (xi - x̄)^4'].append(f'= {summation_fi_xi_xbar_to_4}')
    frequency_distribution_table['CFi'].append(f'= {n}')
    frequency_distribution_table['is_median_class'].append(f'-')


    print(tabulate(frequency_distribution_table, headers='keys', tablefmt='grid'))

    # Mean
    print('Mean calculations: ')
    print('Mean, x̄ = (Σ (fi * xi))/n')
    print('n =', n)
    print('Σ (fi * xi) =', summation_fi_xi)
    print('Mean =', x_mean)
    print()

    # Median
    print('Median calculations: ')
    print('Estimated Median = L + (((n/2) - B) / G) * w')
    print('L =', L)
    print('B =', B)
    print('G =', G)
    print('w =', w)
    print('Median =', median)
    print()

    # Variance and Standard Deviation
    print('Variance and Standard Deviation: ')
    print('Variance = (Σ (fi * (xi - x̄)^2)) / (n - 1)')
    print('n - 1 =', n - 1)
    print('Σ (fi * (xi - x̄)^2) =', summation_fi_xi_xbar_squared)
    print('Variance =', variance)
    print('Standard Deviation, s =', standard_deviation)
    print()

    # Skewness
    print('Skewness: ')
    print('Skewness = (Σ (fi * (xi - x̄)^3)) / ((n - 1) * s^3)')
    print('Σ (fi * (xi - x̄)^3) =', summation_fi_xi_xbar_cubed)
    print('n - 1 =', n - 1)
    print('s =', standard_deviation)
    print('Skewness =', skewness)
    print()

    # Kurtosis
    print('Kurtosis: ')
    print('Kurtosis = (Σ (fi * (xi - x̄)^4)) / ((n - 1) * s^4)')
    print('Σ (fi * (xi - x̄)^4) =', summation_fi_xi_xbar_to_4)
    print('n - 1 =', n - 1)
    print('s =', standard_deviation)
    print('Kurtosis =', kurtosis)
    print()

    print('-----------------------------------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    given_dataset = get_extracted_data(
        raw_dataset='''21 43 21 25 26 28 25 29 30 33
26 38 44 37 27 32 33 28 41 28
23 39 23 35 25''',
        type_cast_to=int
    )

    complete_table_from_class_interval(
        class_interval_list=[[20, 25], [25, 30], [30, 35], [35, 40], [40, 45]],
        dataset=given_dataset
    )

    # generate_frequency_distribution_table(
    #     dataset=given_dataset,
    #     interval_range=5,
    #     is_exclusive=False
    # )

    # complete_table_from_frequency_distribution(
    #     class_interval_list=[[20, 25], [25, 30], [30, 35], [35, 40], [40, 45]],
    #     frequency_list=[4, 10, 4, 4, 3]
    # )

    # complete_table_from_frequency_distribution(
    #     class_interval_list=[[51, 55], [56, 60], [61, 65], [66, 70]],
    #     frequency_list=[2, 7, 8, 4]
    # )

    # complete_table_from_class_interval(
    #     class_interval_list=[[31, 39], [39, 47], [47, 55], [55, 63], [63, 71]],
    #     dataset=[39, 43, 47, 50, 53, 53, 55, 58, 58, 61, 61, 62, 63, 63, 67]
    # )
