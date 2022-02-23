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


def generate_frequency_distribution_table(dataset, interval=10, is_exclusive=True):
    n = len(dataset)
    lowest_data = min(dataset)
    highest_data = max(dataset)

    get_limits = get_highest_limit(lowest_data, highest_data, interval)

    lowest_limit = get_limits['lower_limit']
    highest_limit = get_limits['upper_limit']

    frequency_distribution_table = {
        'Class Interval': [],
        'frequency (f)': [],
        'midpoint (x)': [],
        'fi * xi': [],
        'fi * (xi - x-bar)^2': [],
        'CFi': [],
    }

    summation_fi_xi = 0

    for i in range(lowest_limit, highest_limit + 1, interval):
        lower_limit = i
        upper_limit = i + interval - 1 if is_exclusive else i + interval

        # frequency_distribution_table['Class Interval'].append(f'{lower_limit} - {upper_limit}')
        frequency_distribution_table['Class Interval'].append([lower_limit, upper_limit])

        frequency_count = 0

        for data in dataset:
            if lower_limit <= data <= upper_limit:
                frequency_count += 1

        frequency_distribution_table['frequency (f)'].append(frequency_count)
        midpoint = (lower_limit + upper_limit)/2
        frequency_distribution_table['midpoint (x)'].append(midpoint)

        fi_xi = frequency_count * midpoint
        frequency_distribution_table['fi * xi'].append(fi_xi)
        summation_fi_xi += fi_xi

    x_mean = summation_fi_xi / n

    j = 0
    cumulative_frequency = 0
    summation_fi_xi_xbar_squared = 0

    for i in range(lowest_limit, highest_limit + 1, interval):
        frequency = frequency_distribution_table['frequency (f)'][j]
        x = frequency_distribution_table['midpoint (x)'][j]
        cumulative_frequency += frequency
        fi_xi_xbar_squared = frequency * ((x - x_mean) ** 2)
        summation_fi_xi_xbar_squared += fi_xi_xbar_squared
        frequency_distribution_table['fi * (xi - x-bar)^2'].append(fi_xi_xbar_squared)
        frequency_distribution_table['CFi'].append(cumulative_frequency)

        j += 1

    variance = summation_fi_xi_xbar_squared / (n - 1)

    print(tabulate(frequency_distribution_table, headers='keys', tablefmt='grid'))
    print('Σ (fi * xi) =', summation_fi_xi)
    print('mean =', x_mean)
    print('Σ (fi * (xi - x-bar)^2) =', summation_fi_xi_xbar_squared)
    print('variance =', variance)
    print('-----------------------------------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    dataset = []
    generate_frequency_distribution_table(dataset)
