import csv

file_name = 'employees.csv'

new_employees = [
    {
        'имя': 'ольга вячеславовна',
        'должность': 'заместитель начальника',
        'зарплата': 80000
    },
    {
        'имя': 'дмитрий горбачев',
        'должность': 'охранник',
        'зарплата': 40000
    },
]

with open(file_name,'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for item in new_employees:
        writer.writerow([item['имя'], item['должность'], item['зарплата']])

print(f'Данные успешно записаны в файл: {file_name}')