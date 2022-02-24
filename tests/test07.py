from tabulate import tabulate


def get_highest_limit(min_data, max_data, interval):
    lowermost_limit = min_data - (min_data % 10)
    uppermost_limit = lowermost_limit

    while uppermost_limit < max_data:
        print(uppermost_limit)
        uppermost_limit += interval

    print(uppermost_limit)

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

        print(highest_limit + 1)
        print([lower_limit, upper_limit])

        # frequency_distribution_table['Class Interval'].append(f'{lower_limit} - {upper_limit}')
        frequency_distribution_table['Class Interval'].append([lower_limit, upper_limit])

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
    #     # dataset = []
    #     # generate_frequency_distribution_table(dataset)
    import re

    #
    #     unclean_data = '''50     52     53     54     55     65     60     70     48     63
    # 74     40     46     59     68     44     47     56     49     58
    # 63     66     68     61     57     58     62     52     56     58'''
    #
    # clean_data = re.split('\s+', unclean_data)
    #
    # for i in range(len(clean_data)):
    #     clean_data[i] = int(clean_data[i])
    #
    # print(min(clean_data))
    # print(max(clean_data))
    #
    # generate_frequency_distribution_table(
    #     dataset=clean_data,
    #     interval=5,
    #     is_exclusive=False
    # )

    unclean_data = '''185

166

176

145

166

191

177

164

171

174

147

178

176

142

170

158

171

167

180

178

173

148

168

187

181

172

165

169

173

184

175

156

158

187

156

172

162

193

173

183

197

181

151

161

153

172

162

179

188

179'''

    clean_data = re.split('\s+', unclean_data)

    for i in range(len(clean_data)):
        clean_data[i] = int(clean_data[i])

    # print(sorted(clean_data))
    #
    # generate_frequency_distribution_table(
    #     dataset=clean_data,
    #     interval=5,
    #     is_exclusive=True
    # )

    dataset = [2, 4, 8, 11, 14, 16, 20, 28, 25, 40, 30, 48, 5, 22, 29, 13, 22, 17, 17, 7]

    # print(sorted(clean_data))

    generate_frequency_distribution_table(
        dataset=dataset,
        interval=5,
        is_exclusive=True
    )
