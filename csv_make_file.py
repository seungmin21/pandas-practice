import csv

# 생성할 데이터
data = [
    ['이름', '나이', '직업'],
    ['홍길동', 30, '의사'],
    ['김철수', 25, '교사'],
    ['박영희', 35, '회사원']
]

# 파일명
filename = 'dynamic_csv_example.csv'

# CSV 파일 생성 및 데이터 쓰기
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)

print(f"CSV 파일 '{filename}'이 생성되었습니다.")