import random

from cat import Cat
from hen import Hen
from cow import Cow
from dog import Dog
from datetime import datetime, timedelta

if __name__ == '__main__':

    # створення дат останніх відвідин ветеренара для різних тваринок
    last_vet_check = datetime.now()
    last_vet_check_cat = last_vet_check - timedelta(days=50)
    last_vet_check_hen = last_vet_check - timedelta(days=10)
    last_vet_check_cow = last_vet_check - timedelta(days=900)
    last_vet_check_dog = last_vet_check - timedelta(days=80)


    # створення списку тварин
    animals = [
        Cat('Димок', 3, 'дворняжка', last_vet_check_cat),
        Hen(1, last_vet_check_hen),
        Cow('Бурьонка', 4, last_vet_check_cow),
        Dog('Шарік', 4, 'вівчарка', last_vet_check_dog)
    ]

    # всі можливі варіанти їжі для тварин. Взяті з усіх класів
    food_variants = [
        'трава',
        'м\'ясо',
        'риба',
        'пшоно',
        'зерно',
        'риба',
        'молоко',
        'сіно',
        'chappi',
        'pedigree'
    ]

    what_we_get = list()
    what_they_get = list()

    # поліморфізм - властивість класів, при якому викликаються одноково названі методи та атрибути,
    # але результати відрізняються: 'name' and 'age' in Cat, Hen, Cow; eat(), treat(), say()
    for a in animals:
        a.say(3)
        for food in random.choices(food_variants, k=3):
            a.eat(food)
            what_they_get.append(food)
        what_we_get.append(a.treat())

    print('We get: ', what_we_get)
    print('They get: ', what_they_get)

    # перевірка тварин чи не голодні та чи не потребують відвідин ветеринара
    i = 1
    for a in animals:
        print(f'{i}.{a}')
        if not a.fed_check:
            print(f'  {a.name} голодний/-а! :(')
        if not a.vet_check:
            print(f'  {a.name} має проблеми і потребує відвідання ветеринара!!! >(')
        i += 1