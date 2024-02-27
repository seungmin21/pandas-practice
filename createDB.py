import pandas as pd
import sqlite3

# 연결점 없으면 파일 생성
conn = sqlite3.connect("database.db")

# 객체 생성
cur = conn.cursor()

# 생성
cur.execute("CREATE TABLE student(id, name, age)")

# value 생성
cur.execute("INSERT INTO student values('5', 'oh', 55)")

# 선택
cur.execute("SELECT * FROM student")


conn.close()

print("테이블 생성 및 데이터 삽입이 완료되었습니다.")