import csv


employees_list = [
    {
        'имя': 'константин петрович',
        'должность': 'уборщик',
        'зарплата': 20000
    },
    {
        'имя': 'елена александровна',
        'должность': 'начальник',
        'зарплата': 110000
    },
    {
        'имя': 'анастасия васильевна',
        'должность': 'секретарь',
        'зарплата': 70000
    },
]

file_name = 'employees.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['имя', 'зарплата', 'должность']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for item in employees_list:
        writer.writerow(item)

print(f'Создан новый файл: {file_name}')