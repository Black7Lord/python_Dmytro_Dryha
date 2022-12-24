def get_float_from_user(comment: str, lower: float = -10, upper: float = 100) -> float: # за замовчуванням
    x = ''
    while True: # not isinstance(x, float)
        try:
            x = input(f'{comment} Input float number: ')
            x = float(x)
            if x < lower or x > upper:
                raise ValueError
            return x
        except Exception:
            print(f'Incorrect input! We expect a number more than {lower}, but less than {upper}')

my_number = get_float_from_user('Hello!', 1, 5)
print(my_number)
print(get_float_from_user('Hi!'))
print(get_float_from_user('Hi there!', lower=1, upper=5))


