# способи обміну даними між користувачем та ПЗ
# перший спосіб введення/виведення даних
#   input()
#   print()
# другий - через графічну оболонку
# третій - через Інтернет, адресу в мережі
# четвертий - введення/виведення даних в/з текстового файлу
import os.path


def read_file(filename: str):
    with open(filename) as f:
        # mode: r, w, a
        print(f, type(f))

        x = f.read(10)
        # EOF - end of file, службовий символ в кінці файлу
        while x:
            print(x)
            x = f.read(5)

        f.close()
        print('File is over!')

def readlines_file(filename: str):
    """
    Читає файл, користуючись readlines()
    :param filename: ім'я файлу
    """
    with open(filename) as f:
        for x in f.readlines():
            print(x, end='')    # end для того, щоб не було перенесень
        f.close()
        print("\n******************")

def readline_file(filename: str):
    """
    Читає файл, користуючись readline()
    :param filename: ім'я файлу
    """
    with open(filename, mode='r', encoding='utf-8') as f: # utf-8 щоб працювати з кирилецею
        for x in f.readline():
            for word in x.split():
                print(word, end='')
        f.close()

def write_file(filename: str):
    with open(filename, mode='w') as f:
        f.write('Hello File!\n')
        f.write('How are you?')

def rewrite_file(filename_a: str, filename_b: str):
    """
    Записує з 'a' в 'b'
    :param filename_a: a
    :param filename_b: b
    """
    with open(filename_a, encoding='utf-8') as f_a:
        with open(filename_b, encoding='utf-8', mode='w') as f_b:
            for line in f_a.readlines():
                f_b.write(line)

#def writelines_file(filename: str, text_to_write: list):
    #with open(filename_a, mode='w', encoding='utf-8') as f:

def write_append_file(filename: str, text_to_write: str):
    """
    Додає рядок до файлу.
    :param filename:
    :param text_to_write:
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        f.write(text_to_write)

if __name__ == '__main__':
    read_file('text_file.txt')
    readlines_file('text_file.txt')
    readline_file('text_file.txt')

    write_file('new_text_file.txt')
    rewrite_file('new_text_file.txt', 'b_text_file.txt')

    write_append_file('app_text.txt', 'Hello, nigga!')

    os.path.join('..', 'LICENSE') # ../LICENSE
    '\n'.join(['first line', 'second line', 'third line'])

    #f = open('text_file.txt', mode='w')