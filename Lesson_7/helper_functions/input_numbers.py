def get_int_from_user(comment: str, lower: int = float('-inf'), upper: int = float('inf')) -> int: # за замовчуванням
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

print('Filename:', __name__)