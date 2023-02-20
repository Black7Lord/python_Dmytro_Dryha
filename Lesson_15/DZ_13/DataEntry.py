import json
import csv
import os
from datetime import date
from datetime import time

from DirectoryProcessor import DirectoryProcessor


class DataEntry:
    """
    Class to represent a single data entry.
    """

    def __init__(self, date: date, time: time, sku: str, warehouse: str,
                 warehouse_cell_id: str, operation: str, invoice: str,
                 expiration_date: date, operation_cost: float, comment: str):
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment

if __name__ == '__main__':
    dp = DirectoryProcessor('SKU')
    dp.read_directory()
    print(dp.get_data()[0])
