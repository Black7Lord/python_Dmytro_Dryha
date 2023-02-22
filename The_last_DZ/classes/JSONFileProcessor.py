import json
from classes import FileProcessor
from The_last_DZ.classes.dataEntry import DataEntry


class JSONFileProcessor(FileProcessor):

    def read_file(self):
        """
        Клас для обробки CSV-файлів. Зчитує файл і записує дані до об'єктів DataEntry
        """
        pool_of_notes = json.load(open(self.filename, 'r'))['data']
        for pon in pool_of_notes:
            self.data_entries.append(DataEntry(
                pon['date'],
                pon['time'],
                pon['sku'],
                pon['warehouse'],
                pon['warehouse_cell_id'],
                pon['operation'],
                pon['invoice'],
                pon['expiration_date'],
                pon['operation_cost'],
                pon['comment']
            ))

        # with open(self.filename) as f:
        # json_data = json.load(f)
        # for data in json_data:
        # self.data_entries.append(DataEntry(data))
