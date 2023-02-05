import random

from cat import Cat
from hen import Hen
from cow import Cow
from dog import Dog

if __name__ == '__main__':
    animals = [
        Cat('Димок', 3, 'дворняжка'),
        Hen(1),
        Cow('Бурьонка', 4),
        Dog('Шарік', 4, 'вівчарка')
    ]

    food_variants = [
        'трава',
        'м\'ясо',
        'риба',
        'пшоно',
        'зерно',
        'риба',
        'молоко',
        'сіно'
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