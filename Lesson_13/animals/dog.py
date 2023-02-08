from .animal import Animal
from datetime import datetime

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str, last_vet_check: datetime = None):
        """
        Клас "Собака". Реалізує головні функції тваринки
        :param name: ім'я
        :param age: вік
        :param breed: порода
        :param last_vet_check: останній візит до ветеренара
        """
        super().__init__(f'собака {name}', {'chappi', 'м\'ясо', 'pedigree'}, age)
        self.say_word = 'Гав!'
        self.breed = breed

        # перевірка чи треба відвідати ветеринара. Для собаки я поставив 2 місяці. Робиться відповідна позначка
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference >= 2:
                self.vet_check = False
            else:
                self.vet_check = True

    def treat(self) -> str:
        """
        Метод для догляду за тваринкою
        :return: рядок з реакцією собаки
        """
        print(f'Ви доглядаєте за {self.name}, песик з вами грається і вам обом весело :)')
        return '"Гав!"'