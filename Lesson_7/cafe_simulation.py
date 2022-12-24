from helper_functions import get_int_from_user

def display_menu(menu_cafe):
    """
    стандарт документування функції
    # робота функції
    Гарно відображає пронумероване меню. Завжди додає пункт "Вихід".
    :param menu_cafe: безпосередньо меню, яке відображається
    :return: нічого
    """
    print('Меню: ')
    for i, element in enumerate(menu_cafe):
        print(f'    {i + 1}. {element[0]:17} {element[1]:3.2f} UAH')
    print(f'    {len(menu_cafe) + 1}. Вихід')

def purchase_from_menu(pocket_size: float, menu_cafe: list):
    """
    Здійснює купівлю з меню кафе якщо є кошти.
    :param pocket_size: кількість коштів у гаманці
    :param menu_cafe: меню кафе
    :return: нічого
    """
    display_menu(menu_cafe)
    exit_index = len(menu_cafe) + 1
    print(f'У вас є {pocket_size:6.2f} UAH. Що бажаєте замовити?\n')
    menu_index = get_int_from_user('> ', lower=1, upper=exit_index)
    if menu_index == exit_index:
        print('Заходьте ще!')
        exit(0)
    menu_item = menu_cafe[menu_index - 1]
    if pocket_size < menu_item[1]:
        print(f'У вас закінчилися кошти. Ви маєте {pocket_size} UAH.')
        return pocket_size
    else:
        pocket_size -= menu_item[1]
        print(f'Вам буде подано {menu_item[0]}. Бажаєте ще щось?')
        return pocket_size


    return menu_index

