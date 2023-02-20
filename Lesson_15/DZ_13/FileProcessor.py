
import json
import csv
import os

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