import math

from tabulate import tabulate


class FrequencyDistributionTable:
    def __init__(self, dataset: list = None, interval_range: int = 10):
        self.dataset = dataset
        self.interval_range = interval_range
        # self.

    def get_highest_limit(self, min_data, max_data):
        lowermost_limit = min_data - (min_data % 10)
        uppermost_limit = lowermost_limit

        while uppermost_limit < max_data:
            uppermost_limit += self.interval_range

        return {
            'lower_limit': lowermost_limit,
            'upper_limit': uppermost_limit
        }

    def generate_frequency_distribution_table(self, class_interval_list: list = None, frequency_list: list = None, is_exclusive: bool = True):
        frequency_distribution_table = {
            'Class Interval': [],
            'frequency (f)': [],
            'midpoint (x)': [],
            'fi * xi': [],
            'fi * (xi - x̄)^2': [],
            'CFi': [],
            'is_median_class': []
        }

        if class_interval_list and frequency_list:
            n = sum(frequency_list)
            frequency_distribution_table['Class Interval'] = class_interval_list
            frequency_distribution_table['frequency (f)'] = frequency_list

        else:
            n = len(self.dataset)
            lowest_data = min(self.dataset)
            highest_data = max(self.dataset)

            get_limits = self.get_highest_limit(lowest_data, highest_data)

            lowest_limit = get_limits['lower_limit']
            highest_limit = get_limits['upper_limit']

            for interval in range(lowest_limit, highest_limit, self.interval_range):
                lower_limit = interval
                upper_limit = interval + self.interval_range - 1

                frequency_distribution_table['Class Interval'].append([lower_limit, upper_limit if is_exclusive else upper_limit + 1])

                frequency_count = 0

                for data in self.dataset:
                    if lower_limit <= data <= upper_limit:
                        frequency_count += 1

                frequency_distribution_table['frequency (f)'].append(frequency_count)

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
        w = self.interval_range

        median = L + ((midvalue - B)/G) * w

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
    dataset = []

    # FrequencyDistributionTable(
    #     dataset=[125, 183, 96, 161, 129, 190, 100, 158, 143, 175, 141, 202, 183, 145, 181, 149, 142, 138, 155, 182, 148, 199, 129, 169, 188, 128, 185, 182, 189, 143, 148, 151],
    #     interval_range=10
    # ).generate_frequency_distribution_table(is_exclusive=True)

    # generate_frequency_distribution_table(dataset)
    # FrequencyDistributionTable(
    #     interval_range=5
    # ).generate_frequency_distribution_table(
    #     class_interval_list=[[0, 5], [5, 10], [10, 15], [15, 20], [20, 25]],
    #     frequency_list=[3, 5, 7, 8, 2]
    # )

    FrequencyDistributionTable(
        interval_range=5
    ).generate_frequency_distribution_table(
        class_interval_list=[[20, 25], [25, 30], [30, 35], [35, 40], [40, 45]],
        frequency_list=[4, 10, 4, 4, 3],
    )
