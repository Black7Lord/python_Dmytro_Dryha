from animal import Animal

class Hen(Animal):
    def __init__(self, age: int):
        super().__init__('курка', {'пшоно', 'зерно'}, age)
        self.say_word = 'Куд-кудах'

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name} і курка зносить яйце')
        return 'Яйце'