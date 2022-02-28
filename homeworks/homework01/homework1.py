import requests
from tabulate import tabulate
from utility_codes.frequency_distribubtion_table import generate_frequency_distribution_table
from utility_codes.central_tendency import CentralTendency

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/series/schedule?lang=en&seriesId=1296684&fixtures=false'

payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)

response_json = response.json()

dataset_by_grounds = {}

whole_dataset = {
    'match_id': [],
    'first_innings_scores': [],
    'ground': [],
}

matches = response_json['content']['matches']

matches.reverse()


def data_insertion_by_checking_innings(matches, dataset):
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

    return dataset


for c, i in enumerate(matches):
    if matches[c]['status'] != 'ABANDONED':
        if matches[c]['ground']['smallName'] not in dataset_by_grounds:
            dataset_by_grounds[matches[c]['ground']['smallName']] = {
                'match_id': [],
                'first_innings_scores': [],
                'ground': [],
            }

            dataset_by_grounds[matches[c]['ground']['smallName']] = data_insertion_by_checking_innings(
                matches,
                dataset_by_grounds[matches[c]['ground']['smallName']]
            )

        else:
            dataset_by_grounds[matches[c]['ground']['smallName']] = data_insertion_by_checking_innings(
                matches,
                dataset_by_grounds[matches[c]['ground']['smallName']]
            )

        whole_dataset = data_insertion_by_checking_innings(
            matches,
            whole_dataset
        )

if __name__ == '__main__':
    print(tabulate(whole_dataset, headers='keys', tablefmt='grid'))

    generate_frequency_distribution_table(
        dataset=whole_dataset['first_innings_scores'],
        interval_range=10,
        is_exclusive=True
    )

    # Ground based calculations:

    for ground in dataset_by_grounds:
        print('Calculations of', ground)
        print()

        data_insertion = CentralTendency(
            dataset=dataset_by_grounds[ground]['first_innings_scores'],
            sort_datas=True
        )

        print('Scores =', data_insertion.get_sorted_dataset())
        print('N =', data_insertion.get_size_of_dataset())
        print('Mean =', data_insertion.get_mean())
        print()
        print('Median =', data_insertion.get_median())
        print()
        print('Variance =', data_insertion.get_variance())
        print()
        print('Standard Deviation =', data_insertion.get_standard_deviation())
        print()
        print('-------------------------------------------------------------------------------------------------------')
