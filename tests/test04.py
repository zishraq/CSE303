from utility_codes.frequency_distribubtion_table import generate_frequency_distribution_table
import requests

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/series/schedule?lang=en&seriesId=1296684&fixtures=false'

payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)

response_json = response.json()

grounds = {}

matches = response_json['content']['matches']

matches.reverse()

for c, i in enumerate(matches):
    if matches[c]['status'] != 'ABANDONED':
        if matches[c]['ground']['smallName'] not in grounds:
            grounds[matches[c]['ground']['smallName']] = {
                'match_id': [],
                'first_innings_scores': [],
                'ground': [],
            }

            if 1 in matches[c]['teams'][0]['inningNumbers']:
                score = int(matches[c]['teams'][0]['score'].split('/')[0])

                grounds[matches[c]['ground']['smallName']]['match_id'].append(c + 1)
                grounds[matches[c]['ground']['smallName']]['first_innings_scores'].append(score)
                grounds[matches[c]['ground']['smallName']]['ground'].append(matches[c]['ground']['smallName'])

            else:
                score = int(matches[c]['teams'][1]['score'].split('/')[0])

                grounds[matches[c]['ground']['smallName']]['match_id'].append(c + 1)
                grounds[matches[c]['ground']['smallName']]['first_innings_scores'].append(score)
                grounds[matches[c]['ground']['smallName']]['ground'].append(matches[c]['ground']['smallName'])

        else:
            if 1 in matches[c]['teams'][0]['inningNumbers']:
                score = int(matches[c]['teams'][0]['score'].split('/')[0])

                grounds[matches[c]['ground']['smallName']]['match_id'].append(c + 1)
                grounds[matches[c]['ground']['smallName']]['first_innings_scores'].append(score)
                grounds[matches[c]['ground']['smallName']]['ground'].append(matches[c]['ground']['smallName'])

            else:
                score = int(matches[c]['teams'][1]['score'].split('/')[0])

                grounds[matches[c]['ground']['smallName']]['match_id'].append(c + 1)
                grounds[matches[c]['ground']['smallName']]['first_innings_scores'].append(score)
                grounds[matches[c]['ground']['smallName']]['ground'].append(matches[c]['ground']['smallName'])


for ground in grounds:
    generate_frequency_distribution_table(
        dataset=grounds[ground]['first_innings_scores'],
        interval=10,
        is_exclusive=True
    )
