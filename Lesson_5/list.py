# Список має суворий порядок

x = [1, 2, 3]
print(type(x))
print(x[0])

y = list((7, 8, 9))
print(type(y))
print(y[0])
print(y[-1])    # Перший з кінця
print(y[-2])

z = ['list', 23, -0.43, False]
print(z)

s = "I am a programmer"
print(s[0], s[-1])
print(s[::-1])

x[0] = x[-1]
print(x)

y = [1, 2, 3]
y[0], y[2] = y[2], y[0]
print(y)

# slice - діапазон
sorted_marks = [100, 87, 77, 61, 50, 32, 15]
# [<звідки, включно>:<до, виключно>]
print(sorted_marks[0:2])
print(sorted_marks[3:])
print(sorted_marks[:3] + sorted_marks[4:])  # Пропуск четвертого елемента

threshold_value = 60
print(len(sorted_marks))
correct_marks = list()  # Новий список для сортування
i = 0   # iterator
while i < len(sorted_marks):
    if sorted_marks[i] >= threshold_value:
        print(f'{sorted_marks[i]} is bigger than {threshold_value}')
        correct_marks.append(sorted_marks[i])
    i += 1

print(correct_marks)