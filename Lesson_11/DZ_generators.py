def fibonacci(n: int):
    """
    Генератор чисел Фібоначчі.
    :param n: кількість згенерованих чисел
    """
    # число, яке безпосередньо повертатиметься генератором
    number = 0
    # попереднє число
    old_number = 0

    for i in range(n):
        yield number
        # число перед попереднім (2 порядки назад)
        old2_number = old_number
        old_number = number
        number = old_number + old2_number
        # умова для генерування першої одинички. Надалі ця умова буде не дійсна
        if number == 0 and old_number == 0:
            number = 1

def split_string(s: str):
    """
    Генератор слів з введеного рядка.
    :param s: рядок, який розділяється на слова
    """
    # створення списку слів шляхом розділення рядка (у split() можна додати аргументи)
    word_list = s.split()
    for word in word_list:
        yield word

if __name__ == '__main__':
    print('Використання генератора чисел Фібоначчі:')
    for x in fibonacci(13):
        print(x)

    print('\n\nВикористання генератора слів з введеного рядка:')
    for w in split_string('i am generating words from text :3 :7 >('):
        print(w)