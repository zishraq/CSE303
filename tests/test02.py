from tabulate import tabulate
import requests

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/series/schedule?lang=en&seriesId=1296684&fixtures=false'

payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)

response_json = response.json()

dataset = {
    'match_id': [],
    'first_innings_scores': [],
    'ground': [],
}

matches = response_json['content']['matches']

matches.reverse()

for c, i in enumerate(matches):
    if matches[c]['status'] != 'ABANDONED':
        if 1 in matches[c]['teams'][0]['inningNumbers']:
            score = int(matches[c]['teams'][0]['score'].split('/')[0])

            dataset['match_id'].append(c + 1)
            dataset['first_innings_scores'].append(score)
            dataset['ground'].append(matches[c]['ground']['smallName'])

        else:
            score = int(matches[c]['teams'][1]['score'].split('/')[0])

            dataset['match_id'].append(c + 1)
            dataset['first_innings_scores'].append(score)
            dataset['ground'].append(matches[c]['ground']['smallName'])


print(tabulate(dataset, headers='keys', tablefmt='grid'))

n = len(dataset['first_innings_scores'])
lowest_score = min(dataset['first_innings_scores'])
highest_score = max(dataset['first_innings_scores'])

lowest_limit = lowest_score - (lowest_score % 10)
highest_limit = highest_score + (9 - (highest_score % 10))

frequency_distribution_table = {
    'Class Interval': [],
    'frequency (f)': [],
    'midpoint (x)': [],
    'fi * xi': [],
    'fi * (xi - x-bar)^2': [],
    'CFi': [],
}

summation_fi_xi = 0

for i in range(lowest_limit, highest_limit + 1, 10):
    lower_limit = i
    upper_limit = i + 9

    frequency_distribution_table['Class Interval'].append(f'{lower_limit} - {upper_limit}')

    frequency_count = 0

    for first_innings_score in dataset['first_innings_scores']:
        if lower_limit <= first_innings_score <= upper_limit:
            frequency_count += 1

    frequency_distribution_table['frequency (f)'].append(frequency_count)
    midpoint = (lower_limit + upper_limit)/2
    frequency_distribution_table['midpoint (x)'].append(midpoint)

    fi_xi = frequency_count * midpoint
    frequency_distribution_table['fi * xi'].append(fi_xi)
    summation_fi_xi += fi_xi


x_mean = summation_fi_xi/n

j = 0
cumulative_frequency = 0
summation_fi_xi_xbar_squared = 0

for i in range(lowest_limit, highest_limit + 1, 10):
    frequency = frequency_distribution_table['frequency (f)'][j]
    x = frequency_distribution_table['midpoint (x)'][j]
    cumulative_frequency += frequency
    fi_xi_xbar_squared = frequency * ((x - x_mean)**2)
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
