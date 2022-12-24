# "отримати ключ" від бібліотеки
import cafe_simulation
# "зробити копію" в цей файл
from cafe_simulation import purchase_from_menu
from helper_functions import input_numbers
# from helper_functions.input_numbers import get_int_from_user

# import *file* (than - file.keyword)
# from *file/dir* import *keyword* - the best
# from *file/dir* import *keyword* as ... - renaming
# from *file/dir* import * - all

# 4 види всього коду:
# 1. імпорти
# 2. константи (з великох букви)
# 3. код у функціях
# 4. if __name__ == '__main__':

# дані мають бути подалі вд логіки обробки

if __name__ == '__main__':

    menu_cafe = [
        ('Американо', 30),
        ('Раф', 40),
        ('Зелений чай', 25),
        ('Чай обліпиховий', 30),
        ('Шоколадне печиво', 50),
        ('Круасан', 25),
        ('Пончики', 35)
    ]

    pocket_size = 100
    while True:
        pocket_size = purchase_from_menu(pocket_size, menu_cafe)