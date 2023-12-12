import csv as arrjin


file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = arrjin.reader(file)

    next(reader, None)

    reader = list(reader)
    '''
    имя  - 0
    должность - 1
    зарплата - 2
    '''
    sorted_employees = sorted(reader, key=lambda item: item[2])

    with open('sorted_employees.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = arrjin.writer(new_file)
        fieldnames = ['имя', 'должность']
        writer.writerow(fieldnames)
        writer.writerows(sorted_employees)

    for item in sorted_employees:
        print(item[0], item[1], item[2])