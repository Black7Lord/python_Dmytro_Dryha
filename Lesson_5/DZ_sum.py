"""
# ініціалізую порожній список для зберігання всіх введених чисел
list_num = list()

while True:
    # запит на введення числа
    num = input('Enter your number or "sum": ')
    # перевірка введеного рядка на наявність ключового слова "sum"
    if num == 'sum':
        # додавання всіх чисел, виведення на екран та закінчення циклу
        sum_num = 0.0
        for i in list_num:
            sum_num += float(i)
        print(f"Sum of your numbers: {sum_num}")
        exit(0)

    # спроба додати число до списку у форматі float (як більш універсальному)
    try:
        list_num.append(float(num))
    except Exception:
        # виведення помилки на екран у разі некоректного введення
        print('Enter a number or "sum", please: ')
"""


# ініціалізую порожній список для зберігання всіх введених чисел
list_num = list()
# запит на введення числа
num = input('Enter your number or "sum": ')
while num != 'sum':
    # перевірка введеного рядка на наявність ключового слова "sum"
    if num == 'sum':
        # додавання всіх чисел, виведення на екран та закінчення циклу
        sum_num = 0.0
        for i in list_num:
            sum_num += float(i)
        print(f"Sum of your numbers: {sum_num}")
        exit(0)

    # спроба додати число до списку у форматі float (як більш універсальному)
    try:
        list_num.append(float(num))
    except Exception:
        # виведення помилки на екран у разі некоректного введення
        print('Enter a number or "sum", please: ')

    num = input('Enter your number or "sum": ')