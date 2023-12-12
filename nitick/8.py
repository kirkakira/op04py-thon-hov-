import csv

file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    reader = list(reader)

    for item in reader:
        print(item[0], item[1], item[2])

    remove = input("Введите сотрудника, которого хотите удалить:")

    remove_employees = [item for item in reader if item[1] != remove]

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['имя', 'должность', 'зарплата']
        writer.writerow(fieldnames)
        writer.writerows(remove_employees)
print(f'сотрудник {remove} успешно удален из файла: {file_name}')

for item in remove_employees:
    print(item[0], item[1], item[2])