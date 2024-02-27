import pandas as pd
from pyarrow import csv
import matplotlib.pyplot as plt

# csv 파일 읽기
data = pd.read_csv('./train_and_test2.csv')

# 데이터 확인 
print(data.head())


