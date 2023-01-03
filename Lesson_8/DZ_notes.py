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
def print_earliest(notes: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку їх додавання до словника.
    :param notes: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('earliest:****************')

    # for key, value in list(notes.items())[:count_int]: #теж робочий варіант
    for key, value in islice(notes.items(), count_int):
        print(key)
    # декоративний рядок
    print('*************************')

def print_latest(notes: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у зворотному порядку додавання їх до словника
    (від останнього до найпершого).
    :param notes: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('latest:******************')
    for key, value in islice(notes.items().__reversed__(), count_int):
        print(key)

    # декоративний рядок
    print('*************************')

def print_longest(notes: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку від найдовшого до найкоротшого.
    :param notes: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('longest:*****************')
    for key, value in sorted(notes.items(), key=lambda note: note[1], reverse=True)[:count_int]:
        print(key)

    # декоративний рядок
    print('*************************')

def print_shortest(notes: dict):
    """
    Функція отримує в якості параметру словник записів користувача, викликає
    функцію запиту кількості записів, які необхідно вивести на екран get_count(),
    виводить на екран записи користувача у порядку від найкоротшого до найдовшого.
    :param notes: словник записів користувача
    :return: нічого
    """
    count_int = get_count()

    # декоративний рядок
    print('shortest:****************')
    for key, value in sorted(notes.items(), key=lambda note: note[1])[:count_int]:
        print(key)

    # декоративний рядок
    print('*************************')

if __name__ == '__main__':
    # створюємо порожній словник
    notes = dict()

    # починаємо цикл введення команд/нотаток
    while True:
        # виведення запрошення ввести команду. Команда може бути словом або цифрою
        command = input('Enter your command:\n\t1. add\n\t2. earliest\n\t3. latest\n\t4. longest\n\t5. shortest'
                        '\n\t6. stop or exit\n>>>').lower()
        # початок перевірки введеного слова на наявність ключових слів/цифр
        if command == 'add' or command == '1':
            input_note = input('\tEnter your note: ')
            # додаємо запис до словника, де ключем буде сам запис, а значенням - його довжина
            notes.update({input_note: len(input_note)})
        else:
            if command == 'earliest' or command == '2':
                print_earliest(notes)
            else:
                if command == 'latest' or command == '3':
                    print_latest(notes)
                else:
                    if command == 'longest' or command == '4':
                        print_longest(notes)
                    else:
                        if command == 'shortest' or command == '5':
                            print_shortest(notes)
                        else:
                            if command == 'exit' or command == 'stop' or command == '6':
                                exit(0)