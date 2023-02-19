class DataEntry:
    def __init__(self, data_dict):
        self.data = data_dict

import csv
import json


class CSVFileProcessor:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield DataEntry(row)


class JSONFileProcessor:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            for entry in data:
                yield DataEntry(entry)

import os


class FileProcessor:
    @staticmethod
    def get_file_processor(file_path):
        extension = os.path.splitext(file_path)[1].lower()

        if extension == '.csv':
            return CSVFileProcessor()
        elif extension == '.json':
            return JSONFileProcessor()
        else:
            raise ValueError(f"Unsupported file extension: {extension}")

    @staticmethod
    def read_directory(directory_path):
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                processor = FileProcessor.get_file_processor(file_path)
                for entry in processor.read_file(file_path):
                    yield entry

if __name__ == '__main__':
    directory_path = 'SKU'
    file_processor = FileProcessor()
    for entry in file_processor.read_directory(directory_path):
        # process data entry here
        print(entry.data)