import csv

file_name = 'employees.csv'

name = input("Введите имя: ")
post = input("Введите должность: ")
salary = input("Введите зарплата: ")

with open(file_name, 'a', newline='',  encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([name, post, salary])

print(f'сотрудник {name}, успешно добавлен в файл: {file_name}')