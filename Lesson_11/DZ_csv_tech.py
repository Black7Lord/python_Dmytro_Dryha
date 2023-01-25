import csv
from uuid import uuid4

def create_index(tech_uids: dict, index_key: str) -> dict:
    """
    Функція створює індекс по категоріям/брендам.
    :param tech_uids: індекс унікальних айді для кожного запису
    :param index_key: рядок-назва категорії/бренду
    :return: new_index: створений індекс по категоріям/брендам
    """
    new_index = dict()
    for uid, tech in tech_uids.items():
        if tech[index_key] in new_index:
            new_index[tech[index_key]].append(uid)
        else:
            new_index[tech[index_key]] = [uid]
    return new_index

def brands_in_category_view(
        tech_uids: dict, _category_index: dict,
        _category_name: str, debug: bool = False
) -> dict:
    """
    Функція рахує кількість брендів у вказаній категорії.
    У словнику, що повертається, будуть лише ті бренди, які є у категорії, а не всі.
    :param _category_name: ім'я категорії
    :param _category_index: індекс категорії
    :param tech_uids: індекс унікальних айді для кожного запису
    :param debug: прапорець для перевірки коректної роботи
    :return: brands_in_category: словник, де ключ - бренди у категорії, а значення - їхня кількість
    """
    brands_in_category = dict()
    for _uid in _category_index[_category_name]:
        if debug:
            print(tech_uids[_uid])
        tech_brand = tech_uids[_uid]['brand']
        if tech_brand in brands_in_category:
            brands_in_category[tech_brand] += 1
        else:
            brands_in_category[tech_brand] = 1
    return brands_in_category

if __name__ == '__main__':
    data = {
        'data': list()
    }
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['data'].append(row)

    # виведення словника із усіма записами для перевірки (не є частиною ДЗ)
    print('1. ', type(data), data)

    # створення індексу унікальних айді для кожного запису
    tech_ids_index = dict()
    for item in data['data']:
        _uid = uuid4()
        tech_ids_index[_uid] = item

    # створення індексу по брендам та виведення кількості товарів кожного бренду
    brand_index = create_index(tech_ids_index, 'brand')
    for key, value in brand_index.items():
        print(f'2. Від бренду "{key}" є {len(value)} товарів')

    # створення індексу по категоріям та виведення кількості товарів в кожній категорії
    category_index = create_index(tech_ids_index, 'category')
    for key, value in category_index.items():
        print(f'3. Серед категорії "{key}" є {len(value)} товарів')

    # виведення на екран переліку повної інформації про кожний товар одного обраного бренда
    # реалізація вибору бренду шляхом введення числа напроти назви у виведеному списку
    print('Виберіть бренд, товари якого ви хочете побачити:')
    i = 1
    brand = 'Logitech'
    category_list = list(brand_index.keys())

    for b in category_list:
        print(f'{i}. {b}')
        i += 1
    choice_brand = input(">>>")
    try:
        int_choice_brand = int(choice_brand)
        if int_choice_brand > 0 and int_choice_brand <= len(category_list):
            brand = category_list[int_choice_brand - 1]
        else:
            print(f'Невірне значення. Буде виведено товари бренду "{brand}".')
    except Exception:
        print(f'Невірне значення. Буде виведено товари бренду "{brand}".')

    print(f'4. Бренд "{brand}":')
    for uid in brand_index[brand]:
        print(tech_ids_index[uid])

    # виведення на екран переліку повної інформації про кожний товар однієї обраної категорії
    # реалізація вибору категорії шляхом введення числа напроти назви у виведеному списку
    print('Виберіть категорію, з якої ви хочете побачити товари:')
    i = 1
    category = 'Smartphones'
    category_list = list(category_index.keys())

    for c in category_list:
        print(f'{i}. {c}')
        i += 1
    choice_cat = input(">>>")
    try:
        int_choice_cat = int(choice_cat)
        if int_choice_cat > 0 and int_choice_cat <= len(category_list):
            category = category_list[int_choice_cat - 1]
        else:
            print(f'Невірне значення. Буде виведено товари з категорії "{category}".')
    except Exception:
        print(f'Невірне значення. Буде виведено товари з категорії "{category}".')

    print(f'5. Категорія "{category}":')
    for uid in category_index[category]:
        print(tech_ids_index[uid])

    # виведення на екран розподілу товарів по брендам для кожної категорії
    for category_name in category_index.keys():
        print(f'6. У категорії "{category_name}" представлені товари таких брендів: ',
              brands_in_category_view(tech_ids_index, category_index, category_name))