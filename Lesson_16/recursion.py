def f(n:int):
    for i in range(n):
        print(i)

def f_recursive(n:int):
    if n > 0:
        print(n)
        f_recursive(n - 1)

if __name__ == '__main__':
    f(5)
    print('....................')
    f_recursive(5)