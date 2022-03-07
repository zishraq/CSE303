import re


def get_extracted_data(raw_dataset):
    if ',' in raw_dataset:
        clean_dataset = re.split(',\s*', raw_dataset)
    else:
        clean_dataset = re.split('\s+', raw_dataset)

    for i in range(len(clean_dataset)):
        clean_dataset[i] = float(clean_dataset[i])

    return clean_dataset


if __name__ == '__main__':
    result = get_extracted_data(raw_dataset='''6.0

6.5

6.2

5.5

5.8

6.8

3.2

3.5

5.0

6.1

7.0

7.5

5.8

6.6

6.0

5.7

3.0

6.3

7.2

5.3''')

    print(result)
