# Pearson's correlation coefficient

from tabulate import tabulate
import math


def calculate_pearsons_correlation_coefficient(x_data, y_data):
    N = len(x_data)

    table_data = {
        'x': x_data,
        'y': y_data,
        'xi - x-mean': [],
        'yi - y-mean': [],
        '(xi - x-mean) * (yi - y-mean)': [],
        '(xi - x-mean)^2': [],
        '(yi - y-mean)^2': [],
    }

    summation_xi_minus_x_mean_multiply_yi_minus_y_mean = 0
    summation_square_x_mean = 0
    summation_square_y_mean = 0

    x_mean = sum(x_data)/N
    y_mean = sum(y_data)/N

    for i in range(len(x_data)):
        xi_minus_x_mean = x_data[i] - x_mean
        yi_minus_y_mean = y_data[i] - y_mean
        xi_minus_x_mean_multiply_yi_minus_y_mean = xi_minus_x_mean * yi_minus_y_mean
        square_x_mean = (x_data[i] - x_mean) ** 2
        square_y_mean = (y_data[i] - y_mean) ** 2

        table_data['xi - x-mean'].append(xi_minus_x_mean)
        table_data['yi - y-mean'].append(yi_minus_y_mean)
        table_data['(xi - x-mean) * (yi - y-mean)'].append(xi_minus_x_mean_multiply_yi_minus_y_mean)
        table_data['(xi - x-mean)^2'].append(square_x_mean)
        table_data['(yi - y-mean)^2'].append(square_y_mean)

        summation_xi_minus_x_mean_multiply_yi_minus_y_mean += xi_minus_x_mean_multiply_yi_minus_y_mean
        summation_square_x_mean += ((x_data[i] - x_mean) ** 2)
        summation_square_y_mean += ((y_data[i] - y_mean) ** 2)

    variance_x = summation_square_x_mean / (N - 1)
    variance_y = summation_square_y_mean / (N - 1)

    sd_x = math.sqrt(variance_x)
    sd_y = math.sqrt(variance_y)

    r = summation_xi_minus_x_mean_multiply_yi_minus_y_mean / ((N - 1) * sd_x * sd_y)

    print(tabulate(table_data, headers='keys', tablefmt='grid'))
    print()
    print('N =', N)
    print('x mean =', x_mean)
    print('y mean =', y_mean)
    print('Σ ( (xi - x-mean) * (yi - y-mean) ) =', summation_xi_minus_x_mean_multiply_yi_minus_y_mean)
    print('Σ ( (xi - x-mean)^2 ) =', summation_square_x_mean)
    print('Σ ( (yi - y-mean)^2 ) =', summation_square_y_mean)
    print('Variance of X =', variance_x)
    print('Variance of Y =', variance_y)
    print('Standard Deviation of X =', sd_x)
    print('Standard Deviation of Y =', sd_y)
    print('r =', r)


if __name__ == '__main__':
    x_data = [43, 21, 25, 42, 57, 59]
    y_data = [99, 65, 79, 75, 87, 81]

    calculate_pearsons_correlation_coefficient(
        x_data=x_data,
        y_data=y_data
    )
