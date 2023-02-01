from cat import Cat
import random
from datetime import datetime, timedelta


if __name__ == '__main__':
    cats = list()

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


    last_vet_check = datetime.now()
    for name in [
        'Білочка', 'Арабіка', 'Линька', 'Димка', 'Санні', 'Тінь', 'Бланка', 'Лілі', 'Луна'
    ]:
        last_vet_check -= timedelta(days=30)
        cats.append(Cat(
            name=name,
            gender='кішка',
            age=random.randint(0, 13),
            breed='британець',
            preferable_meal=set(random.choices(cat_food, k=5)),
            last_vet_check=last_vet_check
        ))

    # всі їдять
    for cat in cats:
        for food in random.choices(cat_food, k=3):
            cat.eat(food)

    # чи у всіх все добре
    print('*******************************')
    for cat in cats:
        print(cat)
        if not cat.fed_check:
            if cat.gender == 'кіт':
                print('Кіт {cat.name} голодний!')
            elif cat.gender == 'кішка':
                print(f'Кішка {cat.name} голодна!')
        if not cat.vet_check:
            if cat.gender == 'кіт':
                print('Кіт {cat.name} має проблеми і потребує відвідання ветеринара!')
            elif cat.gender == 'кішка':
                print(f'Кішка {cat.name} має проблеми і потребує відвідання ветеринара!')
