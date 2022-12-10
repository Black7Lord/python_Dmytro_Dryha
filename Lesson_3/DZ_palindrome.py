# Виведення запиту на введення рядку
input_str = input('Введіть ваш рядок: ')

# Початок операцій з рядком
# Перетворення у нижній регістр та позбавлення розділових знаків
res_str = input_str.lower().replace(".", '')\
    .replace(",", '')\
    .replace(" ", '') \
    .replace("-", '') \
    .replace(":", '')\
    .replace(";", '')\
    .replace("!", '')\
    .replace("?", '')\
    .replace("'", '')\
    .replace("\"", '')\
    .replace("\n", '')\
    .replace("\t", '')\
    .strip()                                    # Позбавлення пробілів з обох сторін
print(res_str)

inv_str = res_str[::-1]                         # Інвертація зміненого рядка
print(inv_str)

if res_str == "":                               # Перевірка чи рядок не порожній
    print("Ви не ввели достатньо символів :/")
else:
    if res_str == inv_str:                      # Порівняння зміненого введеного рядка з інвертованим
        print("Введений рядок є паліндромом!")
    else:
        print("Цей рядок не є паліндромом :(")