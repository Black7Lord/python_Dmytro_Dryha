import csv
from classes import FileProcessor
from The_last_DZ.classes.dataEntry import DataEntry

class CSVFileProcessor(FileProcessor):

    def __init__(self, filename):
        """
        Клас для обробки CSV-файлів. Зчитує файл і записує дані до об'єктів DataEntry
        :param filename: ім'я файлу
        """
        super().__init__(filename)

    def read_file(self):
        """
        Метод для зчитування даних з файлу і запису їх до об'єктів DataEntry.
        Сукупність цих об'єктів зберігається до списку data_entries
        """
        with open(self.filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data_entries.append(DataEntry(
                    row['date'],
                    row['time'],
                    row['sku'],
                    row['warehouse'],
                    row['warehouse_cell_id'],
                    row['operation'],
                    row['invoice'],
                    row['expiration_date'],
                    row['operation_cost'],
                    row['comment']
                ))
                #print(type(row), row)
                #self.data['data'].append(row)

                #data['data'].append(row)

            #csv_reader = csv.reader(f, delimiter=self.delimiter)
            #for data in csv_reader:
                #self.data_entries.append(DataEntry(data))