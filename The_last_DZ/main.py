from classes import DirectoryProcessor

# файл запуску
if __name__ == '__main__':
    dp = DirectoryProcessor('SKU')
    dp.read_directory()
    all_data = dp.get_data()

    # перелік полів у записах
    FIELDS = ('date', 'time', 'sku', 'warehouse', 'warehouse_cell_id', 'operation', 'invoice',
              'expiration_date', 'operation_cost', 'comment')

    # цикл для вибору команди
    while True:
        choice_of_user = input(
            'Введіть команду:\n'
            '\t 1 - Вивести на дисплей всі записи\n'
            '\t 2 - Вивести на дисплей всі записи із зазначеним полем\n'
            '\t 3 - Показати кількість всіх записів\n'
            '\t 4 - Вийти з програми\n'
            '>>>'
        )
        # виведення всіх записів на екран
        if choice_of_user == '1':
            for a in all_data:
                print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                      f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')

        # виведення записів на екран за вказаним полем
        elif choice_of_user == '2':
            entered_field = print('Введіть поле, за яким вивести записи:')
            i = 1
            for field in FIELDS:
                print(f'{i}. {field}')
                i += 1
            entered_field = input('>>>')
            if entered_field in FIELDS or entered_field.isdecimal():
                if entered_field.isdecimal():
                    if not int(entered_field) in range(len(FIELDS) + 1):
                        print('Не коректне введене поле!')
                        continue

                entered_field_value = input('Введіть значення поля для пошуку:\n>>>')

                i = 0
                if entered_field == 'date' or entered_field == '1':
                    for a in all_data:
                        if entered_field_value == a.date:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'time' or entered_field == '2':
                    for a in all_data:
                        if entered_field_value == a.time:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'sku' or entered_field == '3':
                    for a in all_data:
                        if entered_field_value == a.sku:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'warehouse' or entered_field == '4':
                    for a in all_data:
                        if entered_field_value == a.warehouse:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'warehouse_cell_id' or entered_field == '5':
                    for a in all_data:
                        if entered_field_value == a.warehouse_cell_id:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'operation' or entered_field == '6':
                    for a in all_data:
                        if entered_field_value == a.operation:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'invoice' or entered_field == '7':
                    for a in all_data:
                        if entered_field_value == a.invoice:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'expiration_date' or entered_field == '8':
                    for a in all_data:
                        if entered_field_value == a.expiration_date:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'operation_cost' or entered_field == '9':
                    for a in all_data:
                        if entered_field_value == a.operation_cost:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
                elif entered_field == 'comment' or entered_field == '10':
                    for a in all_data:
                        if entered_field_value == a.comment:
                            print(f'{a.date}, {a.time}, {a.sku}, {a.warehouse}, {a.warehouse_cell_id}, {a.operation}, '
                                  f'{a.invoice}, {a.expiration_date}, {a.operation_cost}, {a.comment}')
                            i += 1
                    print(f'Всього знайдено {i} записів')
            else:
                print('Не коректне введене поле!')

        # виведення кількості всіх записів
        elif choice_of_user == '3':
            print(f'Кількість зчитаних записів: {len(all_data)}')

        # вихід з програми
        elif choice_of_user == '4':
            exit(0)