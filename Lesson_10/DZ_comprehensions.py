# оголошення константи-файлу
FILENAME = 'testfile.txt'

if __name__ == '__main__':
    # відкриваємо файл для читання
    with open(FILENAME, encoding='utf-8') as f:
        # створюємо список рядків:
        # обрізаємо по літеру 'a', видаляємо символ перенесення на новий рядок,
        # робимо першу літеру великою, а решту - маленькими.
        list_lines = [line[line.find('a'):].replace('\n', '').capitalize() for line in f.readlines()]
        print(list_lines)

"""
Вміст testfile.txt:

gfhdaDSXd
asdjhdx
sdjhAxdzx
sdkcxnz
23lk20::fds
AAAA
dsalk,c;'
"""