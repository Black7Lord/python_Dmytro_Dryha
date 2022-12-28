# імпортую функцію знаходження кореня квадратного з модулю math
from math import sqrt

# функція введення сторони трикутника
def enter_side(message: str) -> int:
    while True:
        size = input(message)
        try:
            temp_size = int(size)
            # перевірка чи додатнє число
            if temp_size <= 0:
                print('Сторона трикутника не може бути від\'ємною або дорівнювати нулю :(')
                continue
            return temp_size
        except Exception:
            print('Введіть коректний цілочисельний розмір сторони!(')

# функція підтверження можливого існування трикутника
def is_real(side1: int, side2: int, side3: int) -> bool:
    if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side1 + side2:
        return False
    return True

# функція знаходження периметру трикутника
def find_perimeter(side1: int, side2: int, side3: int) -> int:
    return side1 + side2 + side3

# функція знаходження площі трикутника за формулою Герона
def find_area(side1: int, side2: int, side3: int) -> float:
    p = find_perimeter(side1, side2, side3) / 2
    s = sqrt(p * (p - side1) * (p - side2) * (p - side3)) # використання імпортованої функції sqrt()
    return s

if __name__ == '__main__':
    size1 = enter_side('Введіть сторону 1 трикутника: ')
    size2 = enter_side('Введіть сторону 2 трикутника: ')
    size3 = enter_side('Введіть сторону 3 трикутника: ')
    print(f'Введені вами значення: {size1}, {size2}, {size3}')

    if is_real(size1, size2, size3):
        print(f'Трикутник зі сторонами {size1}, {size2}, {size3} може існувати :)')
    else:
        print(f'Трикутник зі сторонами {size1}, {size2}, {size3} НЕ може існувати :(')
        exit(0)

    per = find_perimeter(size1, size2, size3)
    print(f'Периметр даного трикутника складає {per}')

    tri_area = find_area(size1, size2, size3)
    print(f'Площа даного трикутника складає {tri_area:.1f}')