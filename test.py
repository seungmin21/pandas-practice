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


