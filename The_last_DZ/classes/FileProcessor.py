class FileProcessor:

    def __init__(self, filename):
        """
        Клас обробки файлів із записами. Є батьківським класом для CSVFileProcessor та JSONFileProcessor
        :param filename: ім'я файлу
        """
        self.filename = filename
        self.data_entries = list()

