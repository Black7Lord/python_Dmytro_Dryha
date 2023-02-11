from fileinput import filename


def my_decorator(func):
    return func


@my_decorator # отримує функцію та всі її параметри
def my_function():
    pass

class CsvFileProcessor:
    FOLDER_IN = 'csv_files'

    def __init__(self, csv_headers):
        self.headers = csv_headers

    # декоратор для позначення методів, що не потребують контексту класу
    @staticmethod
    def peek_headers(filename: str):
        with open(filename, newline='') as csv_file:
            pass
        headers = ['header1', 'header2']#list()
        return headers

    # альтернативний варіант створення класу
    # декоратор приймає ім'я класу та володіє його контекстом
    # частіше використовується при обробці вхідних параметрів для створення об'єкта
    @classmethod
    def create_processor_from_filename(cls, filename: str):
        print(cls == CsvFileProcessor, type(cls), type(CsvFileProcessor))
        header = cls.peek_headers(filename)
        return CsvFileProcessor(header)

if __name__ == '__main__':
    print(CsvFileProcessor.FOLDER_IN)
    print(CsvFileProcessor.peek_headers('csv_files/csv_file.csv'))

    cfp2 = CsvFileProcessor.create_processor_from_filename('csv_files/csv_file.csv')
    print(cfp2)
    print(cfp2.FOLDER_IN)
    print(cfp2.peek_headers('csv_files/csv_file.csv'))
