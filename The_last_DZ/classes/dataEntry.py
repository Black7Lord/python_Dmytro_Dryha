from datetime import date
from datetime import time


class DataEntry:
    def __init__(self, date_de: date, time_de: time, sku_de: str, warehouse_de: str,
                 warehouse_cell_id_de: str, operation_de: str, invoice_de: str,
                 expiration_date_de: date, operation_cost_de: float, comment_de: str):
        """
        Клас для зберігання записів із прочитаних файлів. Містить всі поля, які мають записи
        :param date_de:
        :param time_de:
        :param sku_de:
        :param warehouse_de:
        :param warehouse_cell_id_de:
        :param operation_de:
        :param invoice_de:
        :param expiration_date_de:
        :param operation_cost_de:
        :param comment_de:
        """
        self.date = date_de
        self.time = time_de
        self.sku = sku_de
        self.warehouse = warehouse_de
        self.warehouse_cell_id = warehouse_cell_id_de
        self.operation = operation_de
        self.invoice = invoice_de
        self.expiration_date = expiration_date_de
        self.operation_cost = operation_cost_de
        self.comment = comment_de
