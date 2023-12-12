import csv

file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['имя'], row['должность'], row['зарплата'])
