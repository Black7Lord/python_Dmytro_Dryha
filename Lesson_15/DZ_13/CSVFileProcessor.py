import json
import csv
import os
from FileProcessor import FileProcessor
from DataEntry import DataEntry

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