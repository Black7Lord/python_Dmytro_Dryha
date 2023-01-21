def simple_generator(n):
    for i in range(n):
        yield 'I am generator'

def readlines_generator(filename, bytes):
    """
    Функція реалізує аналог readlines(), але через генератор
    :param filename: ім'я файлу
    :param bytes: скільки символів за раз оброблювати
    :return: генерує рядки файлу
    """
    with open(filename, mode='r') as f:
        s = f.read(bytes)
        i = 0
        # поки не дійшли до кінця файлу
        while s:
            lines = s.split('\n')
            # коли немає перенесень
            if len(lines) == 1:
                s += f.read(bytes)
            # є перенесення на новий рядок
            else:
                # рядок у першому елементі списку
                yield f'{i}. {lines[0]}'
                i += 1
                # зберігаємо для подальшого читання
                s = '\n'.join(lines[1:])
                # якщо інше - порожнеча, читаємо поза чергою щоб не вийти із циклу
                if not s:
                    s = f.read(bytes)

def geom_progression(start_value: float, end_value: float, q: float):
    current_value = start_value
    while current_value < end_value:
        yield current_value
        current_value *= q

if __name__ == '__main__':
    # print(list(simple_generator()))
    for x in simple_generator(5):
        print(x)

    # не виведе значення, не має жодних значень
    y = simple_generator(100)
    print(type(y), y)

    for chunk in readlines_generator('hr_department.csv', 50):
        print(chunk)

    for x in geom_progression(1, 100000000000000000000, 66):
        print(x)