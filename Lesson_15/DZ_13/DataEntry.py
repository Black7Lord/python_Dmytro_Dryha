import json
import csv
import os


class DataEntry:
    """
    Class to represent a single data entry.
    """

    def __init__(self, data):
        self.data = data


class FileProcessor:
    """
    Class to represent a file processor.
    """

    def __init__(self, filename):
        self.filename = filename
        self.data_entries = []

    def read_file(self):
        """
        Reads data from file and appends it to data_entries list.
        """
        raise NotImplementedError


class JSONFileProcessor(FileProcessor):
    """
    Class to represent a JSON file processor.
    """

    def read_file(self):
        """
        Reads data from a JSON file and appends it to data_entries list.
        """
        with open(self.filename) as f:
            json_data = json.load(f)
            for data in json_data:
                self.data_entries.append(DataEntry(data))


class CSVFileProcessor(FileProcessor):
    """
    Class to represent a CSV file processor.
    """

    def __init__(self, filename, delimiter=","):
        super().__init__(filename)
        self.delimiter = delimiter

    def read_file(self):
        """
        Reads data from a CSV file and appends it to data_entries list.
        """
        with open(self.filename) as f:
            csv_reader = csv.reader(f, delimiter=self.delimiter)
            for data in csv_reader:
                self.data_entries.append(DataEntry(data))


class DirectoryProcessor:
    """
    Class to represent a directory processor.
    """

    def __init__(self, directory):
        self.directory = directory
        self.file_processors = []

    def read_directory(self):
        """
        Reads all files in a directory and initializes file_processors list.
        """
        for filename in os.listdir(self.directory):
            if filename.endswith(".json"):
                fp = JSONFileProcessor(os.path.join(self.directory, filename))
                fp.read_file()
                self.file_processors.append(fp)
            elif filename.endswith(".csv"):
                fp = CSVFileProcessor(os.path.join(self.directory, filename))
                fp.read_file()
                self.file_processors.append(fp)

    def get_data(self):
        """
        Returns a list of all data_entries from all file_processors.
        """
        data_entries = []
        for fp in self.file_processors:
            data_entries += fp.data_entries
        return data_entries

if __name__ == '__main__':
    dp = DirectoryProcessor('SKU')
    dp.read_directory()
    print(dp.get_data())
