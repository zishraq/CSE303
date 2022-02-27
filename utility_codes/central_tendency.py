import math


class CentralTendency:
    def __init__(self, dataset: list, sort_datas: bool = True):
        self.sort_datas = sort_datas
        self.dataset = sorted(dataset) if self.sort_datas else dataset
        self.n = len(dataset)

    def get_sorted_dataset(self):
        if not self.sort_datas:
            self.dataset = sorted(self.dataset)

        return self.dataset

    def get_size_of_dataset(self):
        return self.n

    def get_range(self):
        return max(self.dataset) - min(self.dataset)

    def get_mean(self):
        print('Σ xi =', sum(self.dataset))
        return sum(self.dataset) / self.n

    def get_trimmed_mean(self, p):
        for i in range(p):
            self.dataset.pop(0)

        for i in range(p):
            self.dataset.pop()

        return sum(self.dataset) / len(self.dataset)

    def get_median(self):
        if self.n % 2 == 0:
            index2 = self.n // 2
            index1 = index2 - 1

            print(f'{self.dataset[index1]}, {self.dataset[index2]}')
            return (self.dataset[index1] + self.dataset[index2]) / 2

        index = self.n // 2
        return self.dataset[index]

    def get_weighted_mean(self, weights: list):
        for i in range(len(self.dataset)):
            self.dataset[i] *= weights[i]

        print(self.dataset)

        return sum(self.dataset) / sum(weights)

    def get_weighted_median(self, weights: list):
        weight_half = sum(weights)/2

        weight_sum = 0
        index = 0
        for i in range(len(weights)):
            if weight_sum != weight_half:
                weight_sum += weights[i]
                index += 1

        return (self.dataset[index] + self.dataset[index - 1]) / 2

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

    def get_variance(self):
        summation_xi_minus_x_bar_squared = 0
        mean = self.get_mean()

        for i in range(len(self.dataset)):
            summation_xi_minus_x_bar_squared += ((self.dataset[i] - mean) ** 2)

        print('Σ (fi * (xi - x̄)^2) =', summation_xi_minus_x_bar_squared)
        return summation_xi_minus_x_bar_squared / (self.n - 1)

    def get_standard_deviation(self):
        return math.sqrt(self.get_variance())

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


if __name__ == '__main__':
    data_insertion = CentralTendency(
        dataset=[8, 9, 10, 10, 10, 11, 11, 11, 12, 13, 15, 16, 16, 17, 20],
        sort_datas=True
    )

    print('Datas =', data_insertion.get_sorted_dataset())
    print()

    print('###### Mean #####')
    print('Mean =', data_insertion.get_mean())
    print()

    print('###### Median ######')
    print('Median =', data_insertion.get_median())
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
    print('Percentile =', data_insertion.get_percentile(95))
    print()

    print('###### Q1 ######')
    print('Q1 =', data_insertion.get_q1())
    print()

    print('###### Q2 ######')
    print('Q2 =', data_insertion.get_q2())
    print()

    print('###### Q3 ######')
    print('Q3 =', data_insertion.get_q3())
    print()

    print('###### IQR ######')
    print('IQR =', data_insertion.get_iqr())
    print()

