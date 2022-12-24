menu_cafe = [
    ('Американо', 30),
    ('Раф', 40),
    ('Зелений чай', 25),
    ('Чай обліпиховий', 30),
    ('Шоколадне печиво', 50),
    ('Круасан', 25),
    ('Пончики', 35)
]

def display_menu():
    print('Меню: ')
    for i, element in enumerate(menu_cafe):
        print(f'    {i + 1}. {element[0]:17} {element[1]:3.2f} UAH')
    print(f'    {len(menu_cafe) + 1}. Вихід')

def purchase_from_menu():
    global pocket_size
    display_menu()
    exit_index = len(menu_cafe) + 1
    print(f'У вас є {pocket_size:6.2f} UAH. Що бажаєте замовити?\n')
    menu_index = get_int_from_user('> ', lower=1, upper=exit_index)
    if menu_index == exit_index:
        print('Заходьте ще!')
        exit(0)
    menu_item = menu_cafe[menu_index - 1]
    pocket_size -= menu_item[1]
    if pocket_size >= 0:
        print(f'Вам буде подано {menu_item[0]}. Бажаєте ще щось?')
    else:
        print('У вас закінчилися кошти. Виходьте геть звідси!(')
        exit(0)

    return menu_index

def get_int_from_user(comment: str, lower: float = 0, upper: float = 1000000) -> int: # за замовчуванням
    x = ''
    while True: # not isinstance(x, float)
        try:
            x = input(f'{comment} Введіть ціле число: ')
            x = int(x)
            if x < lower or x > upper:
                raise ValueError
            return x
        except Exception:
            print(f'Некоректне значення! Введіть число більше за {lower}, але менше ніж {upper}.')

if __name__ == '__main__':
    pocket_size = 100
    while True:
        purchase_from_menu()