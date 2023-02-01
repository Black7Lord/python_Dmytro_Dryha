from datetime import datetime

class Cat:
    # конструктор класу для створення об'єктів та заповнення полів
    # self - сам об'єкт класу
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
        Кіт або кішка, відповідає за основні елементи життєдіяльності.
        :param name:
        :param gender:
        :param age:
        :param breed:
        :param preferable_meal:
        :param last_vet_check: дата останньої перевірки
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.preferable_meal = preferable_meal
        self.fed_check = True

        if isinstance(last_vet_check, datetime):
            # month_difference = datetime.now().month - last_vet_check.month
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference > 6:
                self.vet_check = False
            else:
                self.vet_check = True
            # datetime.now().month
            # self.vet_check


    def __str__(self):
        return f'{self.gender} породи {self.breed} звати {self.name} вік {self.age}'

    def sleep(self, hours: int):
        """
        Кіт спить. Чим старший, тим більше спить
        :param hours: скільки годин спить
        :return:
        """
        if self.age > 2:
            hours += 2
        elif self.age > 8:
            hours += 4
        print(f'{self.name} спить {hours} годин')

    def eat(self, food: str):
        """
        Кіт їсть
        :param food:
        :return:
        """
        if food in self.preferable_meal:
            print(f'{self.name} їсть {food}')
            self.fed_check = True
        else:
            print(f'{self.name} проходить повз {food} та нічого не їсть :(')
            self.meow(3)
            self.fed_check = False

    def meow(self, count: int):
        """
        Кіт мявкає count разів
        :param count:
        :return:
        """
        for i in range(count):
            print(f'{self.name} мявкає')
    #pass

