from random import shuffle, choice, choices

marks = [100, 87, 77, 61, 50, 32, 15]
shuffle(marks)
correct_marks = list()
threshold = 60

for m in marks:
    if m >= threshold:
        correct_marks.append(m)
        # не рекомендовано: correct_marks += m

print(correct_marks)

apple_weights = list(marks)
print(apple_weights)
max_apple = 0
for apple_weight in apple_weights:
    if max_apple < apple_weight:
        max_apple = apple_weight
print(max_apple)

print(max(apple_weights))
print(min(apple_weights))

print(choice(apple_weights))
print(choices(apple_weights, k = 3))

# повертає список, але не змінює його
print(sorted(apple_weights))
print(sorted(apple_weights, reverse=True))

# сортує сам список, не повертає значення
apple_weights.sort()
print(apple_weights)
apple_weights.reverse()
print(apple_weights)

# вирізає окремий елемент списку
apple_weights.pop(3)
print(apple_weights)

x = [5, 6, 7]
y = [9, 8, 9]
print(x + y)
y.extend(x)
print(y)