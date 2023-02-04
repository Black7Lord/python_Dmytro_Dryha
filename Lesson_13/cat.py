from animal import Animal

class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(f'Кіт {name}', {'риба', 'м\'ясо', 'молоко'}, age)
        self.say_word = 'Мяв'

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name} і вам стає приємно')
        return '"Мурр"'