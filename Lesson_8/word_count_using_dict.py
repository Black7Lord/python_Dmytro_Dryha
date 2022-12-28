large_text = """
Водяні двигуни, найповажніші за віком, справно служать на гідроелектростанціях. За виглядом і за потужністю вони не схожі на стародавні водяні колеса. Сьогодні гідротурбіни — наймогутніші двигуни у світі. Падаюча вода обертає величезні сталеві колеса з лопатями, насадженими на масивний вал. І якщо до цього ж валу приєднати генератор, гідроелектростанція почне виробляти електричний струм.
Такий же принцип дії і у вітряних двигунів, тільки колесо з лопатями обертає не вода, а вітер. За допомогою вітродвигунів можна приводити в дію насоси, що викачують воду з глибоких колодязів, а можна отримувати електричний струм — для цього вал потрібно з'єднати з генератором. Але вітер дме з різною силою в різний час, а то і зовсім стихає. Тому на вітроелектростанціях (ВЕС) ставлять накопичувачі енергії. Наприклад, високо розташовані резервуари з водою. Поки є вітер, частина енергії ВЕС примушує працювати насос, що піднімає воду на велику висоту. Але вітер впав — і вода починає зливатися з резервуару. По дорозі вона обертає турбіну і сполучений з нею генератор.
В інших випадках об'єднують в одну ВЕС декілька вітряних коліс, які працюють далеко одне від одного. І якщо вітер є в районі хоч би одного з коліс, станція не перестає подавати енергію."""

large_text = large_text.lower()
words = large_text.split()
print(f'Символів: {len(large_text)}; слів: {len(words)}')
print(type(words))

alteration_signs = '.,1234567890()[]:;—"/\'\\`'
stop_words = {'на', 'і', 'в', 'за', 'з', ''}
word_population = dict()

for word in words:
    word = word.strip(alteration_signs)
    if word in stop_words:
        continue
    if word in word_population:
        word_population[word] += 1
    else:
        word_population[word] = 1

print(word_population)
print(sorted(list(word_population.items()), key=lambda x: x[1], reverse=True))

word_population_list = list(word_population.items())
word_population_list.sort(key=lambda x:x[1], reverse=True)
print(word_population_list[:5])
print(word_population_list[-5:])