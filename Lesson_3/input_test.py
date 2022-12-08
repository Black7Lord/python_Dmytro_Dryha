x = input("Input smth:")
print(type(x))
print(x.isdigit())
print(x.isnumeric())
print(x.isdecimal())

while not isinstance(x, int):
    try:
        x = input("Input smth:")
        x = int(x)
    except Exception:
        print("Your input was incorrect(")
        # exit(0)