from animal import Animal

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(f'Собака {name}', {'chappi', 'м\'ясо', 'pedigree'}, age)
        self.say_word = 'Гав!'
        self.breed = breed

    def treat(self) -> str:
        print(f'Ви доглядаєте за {self.name}, песик з вами грається і вам обом весело :)')
        return '"Гав!"'