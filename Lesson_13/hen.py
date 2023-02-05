from animal import Animal
from datetime import datetime

class Hen(Animal):
    def __init__(self, age: int, last_vet_check: datetime = None):
        super().__init__('курка', {'пшоно', 'зерно'}, age)
        self.say_word = 'Куд-кудах'
        if isinstance(last_vet_check, datetime):
            month_difference = (datetime.now() - last_vet_check).days // 30
            if month_difference >= 4:
                self.vet_check = False
            else:
                self.vet_check = True

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name} і курка зносить яйце')
        return 'Яйце'