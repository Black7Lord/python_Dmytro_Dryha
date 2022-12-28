def calculate(message: str) -> str:
    # Починається перебір можливих введених значень
    # Якщо введено '1', то почнеться алгоритм для обрахування градусів з радіан
    if type == '1':
        rad = input(message)
        # Головна формула обрахунку градусів
        temp, deg = divmod(float(rad) * 180 / 3.14159, 360)  # Значення більші за 360 будуть округлюватися
        if temp > 0 and deg == 0.0:  # Умова для того, щоб при 2Pi було не 0, а 360
            deg = 360
        return f"{rad} radians = {round(deg, 5)} degrees"

    # Якщо введено '2', то почнеться алгоритм для обрахування радіан з градусів
    if type == '2':
        deg = input(message)
        # Головна формула обрахунку градусів
        temp, rad = divmod(float(deg) * 3.14159 / 180, 6.28318)  # Значення більші за 2Pi будуть округлюватися
        if temp > 0 and rad == 0.0:  # Умова для того, щоб при 360 було не 0, а 6.28318 радіан
            rad = 6.28318
        return f"{deg} degrees = {round(rad, 5)} radians"

    # У разі некоректного введення значення для вибору типу даних з'являється помилка
    if type != '1' and type != '2':
        return 'Bad type of value :('


if __name__ == '__main__':
    # Викликаю вікно діалогу з можливістю вибору типу введених даних
    type = input("""Choose what you will input:
    1. Radians
    2. Degrees
    """)

    print(calculate('Input your value:'))