import json
import csv
import os

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