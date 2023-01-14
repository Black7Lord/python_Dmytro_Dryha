#import path
import os

l = list()
l.append(5)
l = [3, 4, 5, 6]

print(list(range(10)))
print(list(range(5, 10)))
print(list(range(5, 20, 2)))
print(list(range(50, 20, -5)))

l = list()
for el in range(10):
    l.append(el ** 2)
print(l)

# list comprehension - після for - iterable
l_comprehension = [x ** 3 for x in range(10)]
# l_comprehension = [x ** 3 for x in range(10) if x > 2]
print(l_comprehension)

with open(os.path.join('..', 'Lesson_9', 'cafe_menu.txt'), encoding='utf-8') as f:
    clear_lines = [line.strip() for line in f.readlines()]
    print(clear_lines)
    for line in clear_lines:
        print(line)

d = {
    'one': 1,
    'two': 2,
    'three': 3
}

# dict comprehension
d = {line: 0 for line in clear_lines}
print(d)

# set comprehension
s =  {x for x in [5, 2, 2, 4]}
print(type(s), s)

# class 'generator', не зберігає значення, а лише контекст
comprehension = (x ** 2 for x in range(10))
print(type(comprehension), comprehension)
#print(comprehension[0])
for x in comprehension:
    print(x)
    break
for x in comprehension:
    print(x)
    break
for x in comprehension:
    print(x)
    break
# запам'ятовує позицію