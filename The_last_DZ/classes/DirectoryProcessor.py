import os
from classes import JSONFileProcessor
from classes import CSVFileProcessor


class DirectoryProcessor:

    def __init__(self, directory):
        """
        Клас для роботи з директоріями
        :param directory: назва папки
        """
        self.directory = directory
        # список процесорів для подальшої роботи з ними
        self.file_processors = []

    def read_directory(self):
        """
        Метод, що читає всі файли з директорії та запускає процесори для зчитування даних
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
        Метод для отримання списку всіх записів
        :return: entries: list - список записів
        """
        entries = []
        for fp in self.file_processors:
            entries += fp.data_entries
        return entries
