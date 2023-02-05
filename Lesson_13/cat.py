from animal import Animal
from datetime import datetime

class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str, last_vet_check: datetime = None):
        super().__init__(f'кіт {name}', {'риба', 'м\'ясо', 'молоко'}, age)
        self.say_word = 'Мяв'
        self.breed = breed
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference >= 3:
                self.vet_check = False
            else:
                self.vet_check = True

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name} і вам стає приємно')
        return '"Мурр"'