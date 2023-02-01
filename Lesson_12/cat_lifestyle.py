import random
from cat import Cat


if __name__ == '__main__':
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

    cats = [
        Cat(name='Сонік', gender='кіт', age=1, breed='дворняга', preferable_meal=set(random.choices(cat_food, k=5))),
        Cat('Фантомасіна', 'кішка', 13, 'британець', set(random.choices(cat_food, k=5))),
        Cat('Цезарік', 'кіт', 13, 'британець', set(random.choices(cat_food, k=5)))
    ]

    for cat in cats:
        print(cat.name, cat.gender, cat.age)
        cat.meow(random.randint(1, 6))
        for food in random.choices(cat_food, k=3):
            cat.eat(food)
        cat.sleep(random.randint(1, 15))

