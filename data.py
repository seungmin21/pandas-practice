import csv
import pandas as pd

csv_file = './netflix_titles.csv'


with open(csv_file, 'r', encoding='utf-8') as file:
    reader = file
    for row in reader:
        print(row)

