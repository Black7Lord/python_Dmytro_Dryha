# імпортування методу islice з бібліотеки itertools для виведення обмеженої кількості записів
from itertools import islice

def get_count() -> int:
    """
    Функція виводить на екран прохання ввести число записів, які необхідно вивести на екран
    відповідно до обраної команди. Намагається введений рядок конвертувати в int. Якщо не вдало
    або число менше нуля, то виводить на екран помилку з проханням ввести ще раз.
    :return: int - кількість записів, які необхідно вивести на екран
    """
    count = input('How much notes you wanna see? ')
    while True:
        try:
            count_int = int(count)
            if count_int <= 0:
                count = input('Please, enter INT greater than 0! ')
                continue
            break
        except Exception:
            count = input('How much notes you wanna see? Please, enter INT! ')
    return count_int

def print_earliest(ndict: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку їх додавання до словника.
    :param ndict: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('earliest:****************')

    # for key, value in list(ndict.items())[:count_int]: #теж робочий варіант
    for key, value in islice(ndict.items(), count_int):
        print(key)
    # декоративний рядок
    print('*************************')

def print_latest(ndict: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у зворотному порядку додавання їх до словника
    (від останнього до найпершого).
    :param ndict: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('latest:******************')
    for key, value in islice(ndict.items().__reversed__(), count_int):
        print(key)

    # декоративний рядок
    print('*************************')

def print_longest(ndict: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку від найдовшого до найкоротшого.
    :param ndict: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('longest:*****************')
    for key, value in sorted(ndict.items(), key=lambda note: note[1], reverse=True)[:count_int]:
        print(key)

    # декоративний рядок
    print('*************************')

def print_shortest(ndict: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку від найкоротшого до найдовшого.
    :param ndict: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('shortest:****************')
    for key, value in sorted(ndict.items(), key=lambda note: note[1])[:count_int]:
        print(key)

    # декоративний рядок
    print('*************************')

def read_from_file(name_of_file: str) -> dict:
    """
    Функція виводить запрошення ввести назву файлу, намагається зчитати рядки нотаток та повертає сформований словник.
    :param name_of_file: ім'я файлу за замовчуванням
    :return: словник нотаток (або порожній)
    """
    # створюємо порожній словник
    ndict = dict()

    # виведення запрошення ввести назву файлу для зчитування записів
    temp_name = input('Enter filename to read all notes in format <filename.txt>: ').strip()
    if '.txt' in temp_name:
        name_of_file = temp_name
    else:
        print('Wrong format!')
    # намагаємося відкрити файл для зчитування записів
    try:
        with open(name_of_file, encoding='utf-8', mode='r') as f:
            # цикл зчитування записів з файлу до словника
            for line in f.readlines():
                # перевірка та видалення знаку переходу на новий рядок
                if line != '\n':
                    if '\n' in line:
                        line = line.replace('\n', '')
                    ndict.update({line: len(line)})
    # виведення повідомлення у разі помилки зчитування
    except Exception:
        print('Your file is not exist!')
    # виведення назви файлу, з якого відбулося (чи не відбулося) зчитування нотаток
    print(f'From {name_of_file}')
    return ndict

def write_to_file(name_of_file: str):
    """
    Функція виводить запрошення ввести назву файлу, записує нотатки до файлу.
    :param name_of_file: ім'я файлу за замовчуванням
    :return:
    """
    # виведення запрошення ввести назву файлу для зчитування записів
    temp_name = input('Enter filename to write all notes in format <filename.txt>: ').strip()
    if '.txt' in temp_name:
        name_of_file = temp_name
    else:
        print('Wrong format!')

    # збереження записів до файлу
    with open(name_of_file, encoding='utf-8', mode='w') as f:
        for line in notes.keys():
            f.write(line + '\n')
        # виведення назви файлу, у який відбувся запис нотаток
        print(f'See {name_of_file}')

if __name__ == '__main__':
    # назва файлу для зчитування/запису за замовчуванням
    filename = 'notes.txt'
    # виклик функції зчитування з файлу
    notes = read_from_file(filename)

    # починаємо цикл введення команд/нотаток
    while True:
        # виведення запрошення ввести команду. Команда може бути словом або цифрою
        command = input('Enter your command:\n\t1. add\n\t2. earliest\n\t3. latest\n\t4. longest\n\t5. shortest'
                        '\n\t6. save & exit\n>>>').lower()
        # початок перевірки введеного слова на наявність ключових слів/цифр
        if command == 'add' or command == '1':
            input_note = input('\tEnter your note: ')
            # додаємо запис до словника, де ключем буде сам запис, а значенням - його довжина
            notes.update({input_note: len(input_note)})
            print(notes)######
            print(notes.items())######
        elif command == 'earliest' or command == '2':
            print_earliest(notes)
        elif command == 'latest' or command == '3':
            print_latest(notes)
        elif command == 'longest' or command == '4':
            print_longest(notes)
        elif command == 'shortest' or command == '5':
            print_shortest(notes)
        elif command == 'exit' or command == 'save' or command == 'save & exit' or command == '6':
            # виклик функції запису до файлу
            write_to_file(filename)
            exit(0)