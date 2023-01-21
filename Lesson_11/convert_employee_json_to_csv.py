import json
import csv
import os

if __name__ == '__main__':
    json_filename = os.path.join('..', 'Lesson_10', 'hr_department.json')
    json_data = json.load(open(json_filename, 'r'))
    if not json_data['data']:
        print(f'File {json_filename} is empty!')
        exit(-1)
    #print(json_data)

    # отримуємо заголовки таблиці
    fieldnames = list(json_data['data'][0].keys())
    with open('hr_department.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # записуємо заголовки
        writer.writeheader()
        # записуємо рядки
        for row in json_data['data']:
            writer.writerow(row)