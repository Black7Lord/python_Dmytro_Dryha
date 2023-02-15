if __name__ == '__main__':
    with open('text.txt') as f:
        # O(1)
        x = 2
        y = 3
        print(x + y)

        # O(n) - складність алгоритму
        text = f.read().split()
        x = 0
        for word in text:
            x += 1
        print(x)

        # O(n^2) - складність алгоритму
        text = f.read().split()
        x = 0
        for word in text:
            for letter in word:
                x += 1
        print(x)

        # O(n * m)
        for word in text:
            text.count(word)

        # O(n^3)
        for word in text:
            for letter in word:
                word.count(letter)

        # O(logn) < O(n)
        #1 6 20 55 78 103... - числа
        #0 1 2 3 4 5... - індекси