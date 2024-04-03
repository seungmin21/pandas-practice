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

# filtered_data = data['country']
# print(filtered_data)

# selected_column = data['country']
# selected_row = data.loc['South_Korea']
# print(selected_row)
# print(selected_column)

# 두개의 열의 행 데이터를 전체 출력하는 것
# select_data = ['title', 'duration']
# print(data[select_data])


# 최대 값을 새로운 열에 추가하는 형태
# data['numeric'] = data['duration'].str.extract('(\d+)').astype(float)
# max_time_row = data.loc[data['numeric'].idxmax()]

# print(max_time_row)

# 열을 추가 하지 않고 기존의 열의 행에서 최대값 찾는 형태
numeric_values = data['duration'].str.extract('(\d+)').astype(float)
max_value_row = data.loc[numeric_values.idxmax()]
# print(max_value_row)

# 최대값 제외하기
max_value = numeric_values.max()
numeric_values = numeric_values[numeric_values < max_value]

# 다시 최대값 찾기
second_max_value_row = data.loc[numeric_values.idxmax()]

# 결과 출력
print(max_value_row)
print(second_max_value_row)

# 최대값 찾기 없어도 무방
# max_value = numeric_values.max()


# print(data.columns)