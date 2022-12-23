set1 = set([5, 2, 1, 3, 4, 5, 5, 5, 2])
set2 = {5, 2, 1, 3, 4, 5, 5, 5, 2}
set_x = {'hello', 'python', 'world', 'python', 'world'}

print(type(set1), set1)
print(type(set2), set2)

# не можна звертатися за індексом
# print(set1[0])

for i in set1:
    print(i)

if 'java' in set_x:
    print(True)
else:
    print(False)

if 'hello' in set_x:
    print(True)
else:
    print(False)

list_x = ['hello', 'python', 'java']
for i in list_x:
    if i in set_x:
        print(f'{i} is in {set_x}')
    else:
        print(f'{i} is NOT in {set_x}')

set_y = set(list_x)

# перетин
print('intersection: ', set_y.intersection(set_x))
# різниця
print('difference: ', set_x - set_y, set_y - set_x)
print('difference 2: ', set_x.difference(set_y), set_y.difference(set_x))
# об'єднання
print('union: ', set_x.union(set_y))
# симетрична різниця
print('symetric difference: ', set_x.symmetric_difference(set_y))

set_x.remove('world')
print(set_x)

set_x.add('ground')
print(set_x)

# вичавити з початку
x = set_x.pop()
print(x, set_x)

# не можна додавати списки у множини
# set_of_lists = {[3, 1], [2]}