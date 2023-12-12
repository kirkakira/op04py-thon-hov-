import csv

file_name = 'employees.csv'

target_letter = input("Введите букву: ")

with open(file_name, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        employees_name = item[1]
        if employees_name and employees_name.startswith(target_letter):
            print(employees_name)