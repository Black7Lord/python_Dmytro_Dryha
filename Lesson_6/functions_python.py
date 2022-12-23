# сигнатура - ім'я та параметри функції
# анотації потрібні для програмістів
def say_hi(name: str):
    temp = 'smth'
    global tmp
    tmp = 'global tmp'
    print(f"Hello, {name}!")    #capitalize() після name

# print(temp)   зона видимості лише в межах функції
# всередині ф-ї ми можемо лише читати глобальні змінні
# щоб змінювати глобальні змінні всередині ф-ї потрібно використовувати global

tmp = 'smbd'
say_hi('Nigga')
say_hi('Bobo')
say_hi(12345)
say_hi(False)
print(tmp)