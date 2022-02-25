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
        'fi * (xi - x-bar)^2': [],
        'Cumulative Frequency (CFi)': [],
    }

    summation_fi_xi = 0

    for interval in range(lowest_limit, highest_limit, interval_range):
        lower_limit = interval
        upper_limit = interval + interval_range - 1

        # frequency_distribution_table['Class Interval'].append(f'{lower_limit} - {upper_limit if is_exclusive else upper_limit + 1}')
        frequency_distribution_table['Class Interval'].append([lower_limit, upper_limit if is_exclusive else upper_limit + 1])

        frequency_count = 0

        for data in dataset:
            if lower_limit <= data <= upper_limit:
                frequency_count += 1

        frequency_distribution_table['frequency (f)'].append(frequency_count)
        midpoint = (lower_limit + upper_limit) / 2
        frequency_distribution_table['midpoint (x)'].append(midpoint)

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
        frequency_distribution_table['fi * (xi - x-bar)^2'].append(fi_xi_xbar_squared)
        frequency_distribution_table['Cumulative Frequency (CFi)'].append(cumulative_frequency)

    # variance calculation and standard deviation
    variance = summation_fi_xi_xbar_squared / (n - 1)
    standard_deviation = math.sqrt(variance)

    # median calculation
    midvalue = n / 2
    median_class_index = 0

    for cfi in range(len(frequency_distribution_table['Cumulative Frequency (CFi)'])):
        if midvalue <= frequency_distribution_table['Cumulative Frequency (CFi)'][cfi]:
            median_class_index = cfi
            break

    L = frequency_distribution_table['Class Interval'][median_class_index][0]
    B = frequency_distribution_table['Cumulative Frequency (CFi)'][median_class_index - 1]
    G = frequency_distribution_table['frequency (f)'][median_class_index]
    w = interval_range

    median = L + ((midvalue - B)/G) * w

    print(tabulate(frequency_distribution_table, headers='keys', tablefmt='grid'))

    # Mean
    print('Mean calculations: ')
    print('Σ (fi * xi) =', summation_fi_xi)
    print('mean =', x_mean)
    print()

    # Median
    print('Median calculations: ')
    print('L =', L)
    print('B =', B)
    print('G =', G)
    print('w =', w)
    print('median =', median)
    print()

    print('Variance and standard deviation: ')
    print('Σ (fi * (xi - x-bar)^2) =', summation_fi_xi_xbar_squared)
    print('variance =', variance)
    print('standard deviation =', standard_deviation)
    print('-----------------------------------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    dataset = []
    generate_frequency_distribution_table(dataset)
