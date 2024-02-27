import csv
import pandas as pd

csv_file = './netflix_titles.csv'


# with open(csv_file, 'r', encoding='utf-8') as file:
    # reader = file
    # for row in reader:
        # print(row)

# CSV 파일 열기
# with open(csv_file, 'r', encoding='utf-8') as file:
    # reader = csv.DictReader(file)
    # for row in reader:
        # if 'South Korea' in row['country']:
            # print(row)

# print(csv_file)

data = pd.read_csv('./netflix_titles.csv')

# print(data)
# print(data.head())
# print(data.head(20))
# print(data.info())

filtered_data = data['country']
print(filtered_data)

selected_column = data['country']
selected_row = data.loc['South_Korea']
print(selected_row)
print(selected_column)



