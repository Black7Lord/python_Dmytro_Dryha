#print(x) - error
x = 5
print(x + 3)
print('Type for 5:', type(x))
print('Type for 4.5:', type(9 / 2))
print('Type for 5.0:', type(5.0))
print('Type for 10/2:', type(10 / 2))

y = 5.9
y = int(y)
print('int for 5.9:', y)

y = 5.9754
y = round(y, 2)
print('5.9754 after round with 2:', y)

c = 5
c -= 1
print('5 after -= 1:', c)

z = 9 // 2
print('9 afer // 2:', z)

z = 9 % 2
print('9 after % 2:', z)

print('divmod(9, 2):', divmod(9, 2))

d, m = divmod(9, 2)
print('d after divmod(9, 2):', d)

print('5 ** 3:', 5 ** 3)

print('25 ** 1 / 2 =', 25 ** 1 / 2)
print('25 ** (1 / 2) =', 25 ** (1 / 2))

print('pow(5,3) =', pow(5,3))

print('abs(10-100) =', abs(10-100))

print('********** Triangle **********')
# s of triangle
a, b, c = 5, 3, 4
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)
    print('s =', s)
else:
    print("Incorrect triangle!")