import csv
# csv як Excel - таблиці та колонки
# значно ефективніший для пам'яті порівняно з JSON
# \n - кожен новий рядок
# delimiter - кожна нова колонка
# quotechar - екрануючий символ
with open('eggs.csv', newline='') as csvfile:
    spanreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print('1. ')
    for row in spanreader:
        print(', '.join(row))

with open('simple_csv.csv', newline='') as csvfile:
    spanreader = csv.reader(csvfile, delimiter=',', quotechar='"') # стандартні розділові знаки
    print('2. ')
    print(type(spanreader), spanreader)
    for row in spanreader:
        print(', '.join(row))

with open('csv_headers_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print('3. ')
    for row in reader:
        print(type(row), row)
        print(row['first name'], row['last name'])