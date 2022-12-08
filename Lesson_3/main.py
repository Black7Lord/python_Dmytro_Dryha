type = 5       # перезапише type()

s1 = 'String string'
s2 = "string"
s3 ="I've an apple"
s4 ='23" display'
s5 ="23\" display"
s6 = """Hello!
 I`ll find you!"""
s7 = "Hello!" \
"I`ll find you!"

s11 = str(5) # конвертує
print(s11)

s12 = ""    # створює порожній рядок
s13 = str() # створює порожній рядок

# конкатенація
s3s4 = s3 + ' ' + s4
print('s3s4:', s3s4)

s33 = (s3 + '. ') * 3
print(s33)

text1 = ''
text1 += s1 + ' '
text1 += s2 + ' '
text1 += s3 + ' '
print(text1)

if "Hello" in s6:
    print("Yes!")
else:
    print("No(")

print(s1.lower())
print(s1.upper())
print(s1.capitalize()) # лише перша буква всього тексту велика
print(s1.title())      # всі перші букви всіх слів великі

print(s2.islower())
print(s2.isupper())

name1 = "John"
name2 = 'Sarah'
date = "10.12.2022"
text = f"""
Hello, {name2}!
I`m writing to you now, in {date}.
Bye. {name1}.
"""
print(text)

text = text.replace("you", "YOU")
print(text)

s = "    Google   bye         "
print(s.strip(" "))
s = "  __ _  Google   bye   ___  "
print(s.strip(" _"))
print(s.lstrip(" _"))
print(s.rstrip(" _"))

# слайс [start:end:step]
s = "I live in Ukraine"
print(s[0])
print(s[3:8])
print(s[:8])
print(s[:])         #all
print(s[-2])
print(s.find('r'))
print(s.find('in Ukraine'))

s = "1234567890"
print(s[::-1])
print(s[::-2])

s = "dsa.sda dfslfmd m l. dl,l . ;l,, . s"
print(s.split('.'))

s = """
str 1
str 2
str 3
str 4
"""
print(s.split())
print(s.split('\n'))
print(s.split('\t'))

print("\n -".join(s.split()))
print(("\n" + '*' * 10 + "\n").join(s.split()))

print("len of 's' =", len(s))