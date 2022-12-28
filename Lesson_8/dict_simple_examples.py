my_fruits = {'banana': 2, 'apple': 3, 'pineapple': 1}
friends_fruits = {'banana': 1, 'apple': 3, 'cocoa': 4}

for my_fruit_name, my_fruit_quantity in my_fruits.items():
    if my_fruit_name in friends_fruits:
        print(f'We have {my_fruit_name}!')
    else:
        print(f'We DON`T have {my_fruit_name}..(')

print(set(my_fruits.keys()).union(set(friends_fruits.keys())))
print(set(my_fruits.keys()).intersection(set(friends_fruits.keys())))

for name, quantity in friends_fruits.items():
    if name in my_fruits:
        my_fruits[name] += quantity
    else:
        my_fruits[name] = quantity
print(my_fruits)

our_fruits = {**my_fruits, **friends_fruits} # {**my_fruits, 'my_key': 5, **friends_fruits}
print(our_fruits)
for name, quantity in my_fruits.items():
    if name in friends_fruits:
        our_fruits[name] += quantity
print(our_fruits)