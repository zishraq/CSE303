import math
from extract_data import get_extracted_data


class CentralTendency:
    def __init__(self, dataset, sort_datas: bool = True, weights: list = None):
        self.sort_datas = sort_datas

        if type(dataset) == str:
            self.dataset = sorted(get_extracted_data(dataset)) if self.sort_datas else dataset
        else:
            self.dataset = sorted(dataset) if self.sort_datas else dataset

        self.weights = weights
        self.n = len(self.dataset)

    def get_sorted_dataset(self):
        if not self.sort_datas:
            self.dataset = sorted(self.dataset)

        return self.dataset

    def get_range(self):
        return max(self.dataset) - min(self.dataset)

    def get_mean(self, should_print=True):
        if should_print:
            print('Σ xi =', sum(self.dataset))
        return sum(self.dataset) / self.n

    def get_trimmed_mean(self, p):
        dataset_copy = []
        dataset_copy.extend(self.dataset)

        for i in range(p):
            if len(dataset_copy) == 0:
                return 0
            dataset_copy.pop(0)

        for i in range(p):
            if len(dataset_copy) == 0:
                return 0
            dataset_copy.pop()

        if len(dataset_copy) == 0:
            return 0

        return sum(dataset_copy) / len(dataset_copy)

    def get_mode(self):
        maximum_occurrence = max(self.dataset, key=self.dataset.count)

        maximum_count = self.dataset.count(maximum_occurrence)

        result = {
            'datas': [],
            'count': maximum_count
        }

        for data in self.dataset:
            if self.dataset.count(data) == maximum_count and data not in result['datas']:
                result['datas'].append(data)

        return result

    def get_median(self, should_print=True):
        if self.n % 2 == 0:
            index2 = self.n // 2
            index1 = index2 - 1

            if should_print:
                print(f'{self.dataset[index1]}, {self.dataset[index2]}')
            return (self.dataset[index1] + self.dataset[index2]) / 2

        index = self.n // 2
        return self.dataset[index]

    def get_weighted_mean(self, should_print=True):
        for i in range(len(self.dataset)):
            self.dataset[i] *= self.weights[i]

        if should_print:
            print(self.dataset)

        return sum(self.dataset) / sum(self.weights)

    def get_weighted_median(self):
        full_dataset = []

        for data in range(len(self.dataset)):
            for i in range(self.weights[data]):
                full_dataset.append(self.dataset[data])

        median_of_full_dataset = CentralTendency(
            dataset=full_dataset
        ).get_median()

        return median_of_full_dataset

    def get_mean_absolute_deviation(self):
        summation_xi_minus_x_bar = 0

        mean = self.get_mean()

        for i in range(len(self.dataset)):
            summation_xi_minus_x_bar += abs(self.dataset[i] - mean)

        return summation_xi_minus_x_bar / self.n

    def get_median_of_median_absolute_deviation(self):
        median = self.get_median()

        median_absolute_deviation = []

        for i in self.dataset:
            median_absolute_deviation.append(abs(i - median))

        median_of_median_absolute_deviation = CentralTendency(
            dataset=median_absolute_deviation
        ).get_median()

        return median_of_median_absolute_deviation

    def get_variance(self, is_sample=True, should_print=True):
        summation_xi_minus_x_bar_squared = 0
        mean = self.get_mean()

        if is_sample:
            self.n -= 1

        for i in range(len(self.dataset)):
            summation_xi_minus_x_bar_squared += ((self.dataset[i] - mean) ** 2)

        if should_print:
            print('Σ ((xi - x̄)^2) =', summation_xi_minus_x_bar_squared)
        return summation_xi_minus_x_bar_squared / self.n

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample=is_sample, should_print=False))

    def get_percentile(self, percent):
        position = ((percent/100) * self.n) - 1

        actual_position = math.floor(position)
        additional = position - actual_position

        percentile_value = self.dataset[actual_position] + additional * (self.dataset[actual_position + 1] - self.dataset[actual_position])

        return percentile_value

    def get_q1(self):
        return self.get_percentile(25)

    def get_q2(self):
        return self.get_percentile(50)

    def get_q3(self):
        return self.get_percentile(75)

    def get_iqr(self):
        return self.get_q3() - self.get_q1()

    def get_upper_extreme(self):
        return self.get_q3() + self.get_iqr() * 1.5

    def get_lower_extreme(self):
        return self.get_q1() - self.get_iqr() * 1.5

    def get_upper_whisker(self):
        return min(self.get_upper_extreme(), max(self.dataset))

    def get_lower_whisker(self):
        return max(self.get_lower_extreme(), min(self.dataset))

    def get_skewness(self, should_print=True):
        summation_xi_minus_x_bar_cubed = 0
        mean = self.get_mean()

        for i in range(len(self.dataset)):
            summation_xi_minus_x_bar_cubed += ((self.dataset[i] - mean) ** 3)

        if should_print:
            print('Σ (fi * (xi - x̄)^3) =', summation_xi_minus_x_bar_cubed)
        return summation_xi_minus_x_bar_cubed / ((self.n - 1) * (self.get_standard_deviation() ** 3))

    def get_kurtosis(self, should_print=True):
        summation_xi_minus_x_bar_to_4 = 0
        mean = self.get_mean()

        for i in range(len(self.dataset)):
            summation_xi_minus_x_bar_to_4 += ((self.dataset[i] - mean) ** 4)

        if should_print:
            print('Σ (fi * (xi - x̄)^4) =', summation_xi_minus_x_bar_to_4)
        return summation_xi_minus_x_bar_to_4 / ((self.n - 1) * (self.get_standard_deviation() ** 4))


if __name__ == '__main__':
    # given_dataset = [3.0, 3.2, 3.5, 5.0, 5.3, 5.5, 5.7, 5.8, 5.8, 6.0, 6.0, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.0, 7.2, 7.5]
    # given_dataset = [3.0, 3.2, 3.5, 5.0, 5.3, 5.5, 5.7, 5.8, 5.8, 6.0, 6.0, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.0, 7.2, 7.5]
    given_dataset = '''60 75 80 85 90 10 65 70 65 80'''

    data_insertion = CentralTendency(
        dataset=given_dataset,
        sort_datas=True
    )

    print('Datas =', data_insertion.get_sorted_dataset())
    print('n =', data_insertion.n)
    print()

    print('###### Mean #####')
    print('Mean =', data_insertion.get_mean())
    print()

    print('###### Median ######')
    print('Median =', data_insertion.get_median())
    print()

    print('###### Trimmed Mean #####')
    p = 3
    print('p =', p)
    print('Trimmed Mean =', data_insertion.get_trimmed_mean(p))
    print()

    print('###### Mode ######')
    print('Mode =', data_insertion.get_mode())
    print()

    print('###### Variance ######')
    print('Variance =', data_insertion.get_variance())
    print()

    print('###### Standard Deviation ######')
    print('Standard Deviation =', data_insertion.get_standard_deviation())
    print()

    print('###### Mean Absolute Deviation ######')
    print('Mean Absolute Deviation =', data_insertion.get_mean_absolute_deviation())
    print()

    print('###### Median of Median Absolute Deviation ######')
    print('Median of Median Absolute Deviation =', data_insertion.get_median_of_median_absolute_deviation())
    print()

    print('###### Percentile ######')
    percentile = 95
    print(f'Q1 = {percentile} % * {data_insertion.n} = {(percentile / 100) * data_insertion.n}th value')
    print(f'{percentile}th Percentile =', data_insertion.get_percentile(percentile))
    print()

    print('###### Q1 ######')
    print(f'Q1 = 25 % * {data_insertion.n} = {(25/100) * data_insertion.n}th value')
    print('Q1 =', data_insertion.get_q1())
    print()

    print('###### Q2 ######')
    print(f'Q2 = 50 % * {data_insertion.n} = {(50 / 100) * data_insertion.n}th value')
    print('Q2 =', data_insertion.get_q2())
    print()

    print('###### Q3 ######')
    print(f'Q3 = 75 % * {data_insertion.n} = {(75 / 100) * data_insertion.n}th value')
    print('Q3 =', data_insertion.get_q3())
    print()

    print('###### IQR ######')
    print('IQR = Q3 - Q1')
    print('IQR =', data_insertion.get_iqr())
    print()

    print('###### Upper Extreme ######')
    print('Upper Extreme = Q1 + IQR * 1.5')
    print('Upper Extreme =', data_insertion.get_upper_extreme())
    print()

    print('###### Lower Extreme ######')
    print('Lower Extreme = Q3 - IQR * 1.5')
    print('Lower Extreme =', data_insertion.get_lower_extreme())
    print()

    print('###### Upper Whisker ######')
    print('Upper Whisker =', data_insertion.get_upper_whisker())
    print()

    print('###### Lower Whisker ######')
    print('Lower Whisker =', data_insertion.get_lower_whisker())
    print()

    print('###### Skewness ######')
    print('Skewness =', data_insertion.get_skewness())
    print()

    print('###### Kurtosis ######')
    print('Kurtosis =', data_insertion.get_kurtosis())
    print()
