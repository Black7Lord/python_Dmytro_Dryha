# tuple - кортеж. Є індекси. Не редагується! Може містити дублікати

x = (3, 5, [])
print(type(x), x)
print(x[0], x[-1])

# x[0] = 1

x[2].append('hello')
print(x)