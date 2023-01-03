def longest(notes: dict) -> dict:
    return dict()


if __name__ == '__main__':
    notes = dict()

    while True:
        command = input('Enter your command: ').lower()
        if command == 'add':
            input_note = input('\tEnter your note: ')
            notes.update({input_note: len(input_note)})
            print(notes)   ######
        else:
            if command == 'earliest':
                count = input('How much notes you wanna see? ')
                while True:
                    try:
                        count_int = int(count)
                        if count_int < 0:
                            count = input('Please, enter INT greater than 0! ')
                        break
                    except Exception:
                        count = input('How much notes you wanna see? Please, enter INT! ')

                for key, value in notes.items():
                    print(key)
            else:
                if command == 'latest':
                    count = input('How much notes you wanna see? ')
                    for key, value in notes.items().__reversed__():
                        print(key)
                else:
                    if command == 'longest':
                        count = input('How much notes you wanna see? ')
                        for key, value in sorted(notes.items(), key=lambda note: note[1], reverse=True):
                            print(key)
                    else:
                        if command == 'shortest':
                            count = input('How much notes you wanna see? ')
                            for key, value in sorted(notes.items(), key=lambda note: note[1]):
                                print(key)
                        else:
                            if command == 'exit' or command == 'stop':
                                exit(0)