class Animal:
    def __init__(self, name: str, allowed_meal: set, age: int):
        """
        Батьківський клас для всіх тварин
        :param name: ім'я
        :param allowed_meal: улюблена їжа
        :param age: вік
        """
        self.name = name
        self.allowed_meal = allowed_meal
        self.age = age
        self.say_word = '???'
        self.fed_check = True


    def eat(self, food: str):
        """
        Пропонуємо їжу. Тварина може з'їсти або ні, про що робиться відповідна позначка
        :param food: їжа, яку пропонують
        """
        if food in self.allowed_meal:
            print(f'{self.name} їсть {food}')
            self.fed_check = True
        else:
            print(f'{self.name} не знає що робити з {food}')
            self.fed_check = False

    def say(self, count: int):
        """
        Тваринка щось каже або робить дію для того щоб привернути увагу
        :param count: кількість разів
        """
        for i in range(count):
            print(f'{self.name} привертає ваше увагу "{self.say_word}"')

    def treat(self):
        """
        Метод для догляду за тваринкою
        """
        print(f'Ви доглядаєте за {self.name}')

    def __str__(self):
        """
        Метод опису об'єкта
        :return: рядок з описом коротких даних про об'єкт-тваринку
        """
        return f'{self.name} віком {self.age}'