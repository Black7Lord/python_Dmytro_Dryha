from datetime import datetime

class Dog:
    def __init__(
            self,
            name: str,
            gender: str,
            age: int,
            breed: str,
            preferable_meal: set,
            last_vet_check: datetime = None
    ):
        """
        Клас "Пес", відповідає за основні елементи життєдіяльності.
        :param name: ім'я собаки
        :param gender: стать собаки
        :param age: вік собаки
        :param breed: порода собаки
        :param preferable_meal: улюблені страви собаки
        :param last_vet_check: дата останньої перевірки у ветеринара
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.preferable_meal = preferable_meal
        self.fed_check = True
        self.walk_check = False

        # вираховуємо різницю часу між останнім візитом до ветеринара і сьогодні у місяцях
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            # якщо у ветеринара пес був більше ніж 6 місяців тому - робимо позначку
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True

    def __str__(self) -> str:
        """
        Виводить рядок опису об'єкта
        :return: опис собаки
        """
        return f'Собака {self.gender} породи {self.breed} звати {self.name} вік {self.age}'

    def eat(self, food: str):
        """
        Собака їсть. Метод визначає чи є іжа серед улюблених страв і видає відповідну відповідь.
        :param food: їжа, якою хочуть нагодувати собаку
        """
        if food in self.preferable_meal:
            print(f'Собака {self.name} їсть {food}')
            self.fed_check = True
        else:
            print(f'Собака {self.name} проходить повз {food} та нічого не їсть :(')
            self.fed_check = False

    def gav(self, count: int):
        """
        Пес гавкає <count> разів
        :param count: кількість гавкань
        """
        for i in range(count):
            print(f'Собака {self.name} гавкає "Гав!"')

    def walk(self, km: float):
        """
        Собака гуляє <km> кілометрів
        :param km: кількість кілметрів прогулянки
        """
        print(f'Собака {self.name} весело гуляє шляхом довжиною в {km} км')
        self.walk_check = True