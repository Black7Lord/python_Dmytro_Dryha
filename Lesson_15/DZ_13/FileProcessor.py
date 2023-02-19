import csv
import json


class FileProcessor:
    def __init__(self, filename: str):
        self.data = {
            'data': list()
        }

        if filename.endswith('.csv'):
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.data['data'].append(row)

        elif filename.endswith('.json'):
            self.data['data'].append(json.load(open(filename, 'r')))

