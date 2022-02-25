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

    def get_mean(self):
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

        return summation_xi_minus_x_bar_squared / (self.n - 1)

    def get_standard_deviation(self):
        return math.sqrt(self.get_variance())


if __name__ == '__main__':
    data_insertion = CentralTendency(
        dataset=[8, 9, 10, 10, 10, 11, 11, 11, 12, 13],
        sort_datas=True
    )

    print('Scores =', data_insertion.get_sorted_dataset())
    print('Mean =', data_insertion.get_mean())
    print('Median =', data_insertion.get_median())
    print('Variance =', data_insertion.get_variance())
    print('Standard Deviation =', data_insertion.get_standard_deviation())
    print('Mean Absolute Deviation =', data_insertion.get_mean_absolute_deviation())
    print('Median of Median Absolute Deviation =', data_insertion.get_median_of_median_absolute_deviation())
