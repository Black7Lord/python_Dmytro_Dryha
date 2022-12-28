# dictionary - словник або хеш-таблиця
# 2 способи створити словник: написати пари елементів, передати список кортежів з двох елементів
d = dict()
print(d, type(d))

s = {1, 2} # set
print(s, type(s))

d = {
    'key1':'value1',
    'key2':'value2',
    'key2':'value3', # повторний ключ перезаписує попередній!
    'key3':'value3',
    1:32,
    2:'f',
    'f':2,
    True:'true' # буде 1
    # list та інші динамічні типи використовувати в якості ключа не можна
}
print(d, type(d))

print(d['key2'])
print(d.keys())

d[5] = '5th element' # створить новий елемент

for key in d.keys():
    print(d[key])

print(d.values())
print(d.items())

d2 = dict(d.items())
print(type(d2), d2)

if 'key3' in d2:
    print('key3 is in d2')
if 'value3' in d2:
    print('value3 is in d2')
else:
    print('value3 is NOT in d2')

# у set та dict пошук 'in' дуже швидкий
# у list та tuple пошук 'in' повільний