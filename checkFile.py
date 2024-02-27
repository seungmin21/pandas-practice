import pandas as pd
import sqlite3

# 데이터베이스 파일 연결
conn = sqlite3.connect('./example.db')

# 테이블 선택
query = "SELECT * FROM student"
# sql 읽기
data = pd.read_sql(query, conn)

# 연결 닫기
conn.close()

# 출력 데이터의 일부분
print(data.head())