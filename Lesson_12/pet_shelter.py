from cat import Cat
from dog import Dog
import random
from datetime import datetime, timedelta


if __name__ == '__main__':
    cats = list()
    dogs = list()

    # список варіантів їжі для котів
    cat_food = [
        'whiskas',
        'м\'ясо',
        'молоко',
        'риба',
        'вода',
        'сухий корм',
        'purina',
        'club 4 paws',
        'gourmet'
    ]

    # список варіантів їжі для собак
    dog_food = [
        'chappi',
        'м\'ясо',
        'молоко',
        'каша',
        'вода',
        'сухий корм',
        'pedigree',
    ]

    print('*************** Коти ***************')
    last_vet_check = datetime.now()
    for name in [
        'Білочка', 'Арабіка', 'Линька', 'Димка', 'Санні', 'Тінь', 'Бланка', 'Лілі', 'Луна'
    ]:
        last_vet_check -= timedelta(days=30)
        cats.append(Cat(
            name=name,
            gender=random.choice(['кіт', 'кішка']),
            age=random.randint(1, 13),
            breed=random.choice(['британець', 'дворняга', 'персидський']),
            preferable_meal=set(random.choices(cat_food, k=5)),
            last_vet_check=last_vet_check
        ))

    # всі коти їдять
    for cat in cats:
        for food in random.choices(cat_food, k=1):
            cat.eat(food)

    # перевіряємо чи у всіх все добре
    i = 1 # номер для зручності показу записів
    for cat in cats:
        print(f'{i}.{cat}')
        if not cat.fed_check:
            print(f'  {cat.gender} {cat.name} голодний/-а!')
        if not cat.vet_check:
            print(f'  {cat.gender} {cat.name} має проблеми і потребує відвідання ветеринара!')
        i += 1

    print('*************** Собаки ***************')
    last_vet_check = datetime.now()
    for name in [
        'Шарік', 'Боб', 'Рекс', 'Діса', 'Кармель', 'Гунд', 'Термінатор', 'Жучка', 'Морріс'
    ]:
        last_vet_check -= timedelta(days=50) # у кожен запис останній візит був -50 днів від попереднього собаки
        dogs.append(Dog(
            name=name,
            gender=random.choice(['хлопчик', 'дівчинка']),
            age=random.randint(1, 12),
            breed=random.choice(['вівчарка', 'тер\'єр', 'чихуахуа', 'пікінес']),
            preferable_meal=set(random.choices(dog_food, k=3)),
            last_vet_check=last_vet_check
        ))

    # всі їдять
    for dog in dogs:
        for food in random.choices(dog_food, k=1):
            dog.eat(food)

    # всі гавкають
    for dog in dogs:
        dog.gav(random.randint(1, 3))

    # гуляємо лише з 7-ма собаками
    for dog in random.choices(dogs, k=7):
        dog.walk(random.randint(1, 5))

    # перевіряємо чи у всіх все добре
    i = 1 # номер для зручності показу записів
    for dog in dogs:
        print(f'{i}.{dog}')
        if not dog.walk_check:
            print(f'  Собака {dog.name} сьогодні не гуляв/-ла! :(')
        if not dog.fed_check:
            print(f'  Собака {dog.name} голодний/-а! :(')
        if not dog.vet_check:
            print(f'  Собака {dog.name} має проблеми і потребує відвідання ветеринара!!! >(')
        i += 1