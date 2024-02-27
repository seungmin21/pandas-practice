import pandas as pd
from pyarrow import csv
import matplotlib.pyplot as plt

# csv 파일 읽기
data = pd.read_csv('./train_and_test2.csv')

# 데이터 확인 
print(data.head())

# 데이터 요약
print(data.info())

selected_column = data['Age']
# 데이터 열 선택
print(selected_column)

selected_row = data.loc[4]
# 데이터 행 선택
print(selected_row)

filtered_data = data[data['Age'] > 5 ]
# 조건을 통한 필터링
print(filtered_data)

# 데이터 열 합치기
data['Age'] = data['Sex'] + data['Fare']
print(data['Age'])

# 통계 계산
mean_value = data['Age'].mean()
print(mean_value)
