import csv as yeji

new_file_name = input(f'Введите имя нового файла: ')
new_file_name += '.csv'


with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    employees_data = [
        {'имя': 'олег васильевич', 'должность': 'охранник', 'зарплата': 40000},
        {'имя': 'екатерина дружкова', 'должность': 'уборщица', 'зарплата': 30000},
    ]

    writer = yeji.writer(file)
    for item in employees_data:
        writer.writerow([item['имя'], item['должность'], item['зарплата']])

with open(new_file_name, newline='', encoding='utf-8') as file:
    reader = yeji.reader(file)

    for item in reader:
        print(item[0], item[1], item[2])