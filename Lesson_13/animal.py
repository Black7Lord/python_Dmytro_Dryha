class Animal:
    def __init__(self, name: str, allowed_meal: set, age: int):
        self.name = name
        self.allowed_meal = allowed_meal
        self.age = age
        self.say_word = '???'

    def eat(self, food: str):
        """
        Пропонуємо їжу
        :param food:
        :return:
        """
        if food in self.allowed_meal:
            print(f'{self.name} їсть {food}')
        else:
            print(f'{self.name} не знає що робити з {food}')

    def say(self, count: int):
        for i in range(count):
            print(f'{self.name} привертає ваше увагу "{self.say_word}"')

    def treat(self):
        
        print(f'Ви доглядаєте за {self.name}')