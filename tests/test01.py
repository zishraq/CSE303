import requests
import json
import csv
import re

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/series/schedule?lang=en&seriesId=1296684&fixtures=false'

payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)

response_json = response.json()

dataset = []

matches = response_json['content']['matches']

matches.reverse()

for c, i in enumerate(matches):
    if matches[c]['status'] != 'ABANDONED':
        if 1 in matches[c]['teams'][0]['inningNumbers']:
            score = int(matches[c]['teams'][0]['score'].split('/')[0])

            match_data = {
                'match_id': c + 1,
                'first_innings_score': score,
                'ground': matches[c]['ground']['smallName']
            }

        else:
            score = int(matches[c]['teams'][1]['score'].split('/')[0])

            match_data = {
                'match_id': c + 1,
                'first_innings_score': score,
                'ground': matches[c]['ground']['smallName']
            }

        dataset.append(match_data)


json_dataset = json.dumps(dataset, indent=2)
print(json_dataset)

csv_file = "dataset.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['match_id', 'first_innings_score', 'ground'])
        writer.writeheader()
        for data in dataset:
            writer.writerow(data)
except IOError:
    print("I/O error")
