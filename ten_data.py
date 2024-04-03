import csv
import pandas as pd

# CSV 파일 로드
data = pd.read_csv('./netflix_titles.csv')

# "duration" 열의 값을 숫자로 변환하여 추출
numeric_values = data['duration'].str.extract('(\d+)').astype(float)

# 최대값을 찾고 출력하기
max_value_row = data.loc[numeric_values.idxmax()]
print([max_value_row.values.tolist()])  # 최대값을 이차원 배열에 담아 출력

# 2번째부터 10번째 최대값까지 찾고 출력하기
top_10_max_values = []
for _ in range(9):  # 2번째부터 10번째까지 총 9번 반복
    # 찾은 최대값을 제외하기
    max_value = numeric_values.max()
    numeric_values = numeric_values[numeric_values < max_value]
    # 다음 최대값 찾기
    max_value_row = data.loc[numeric_values.idxmax()]
    # 결과 리스트에 추가
    top_10_max_values.append(max_value_row.values.tolist())  # 최대값을 이차원 배열에 담아 추가

# 결과 출력 (이차원 배열 형태로 출력)
print(top_10_max_values)

