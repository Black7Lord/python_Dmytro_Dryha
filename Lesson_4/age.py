"""
if <cond>:
    <body of if>
elif <cond>:
    <body of elif>
elif <cond>:
    <body of elif>
...
elif <cond>:
    <body of elif>
else:
    <body of else>
"""

while True:
    try:
        age_of_user = int(input("Введіть свій вік: "))
    except Exception:
        print("Enter valid number, pls!")
        continue
    if age_of_user < 0:
        print("Are you OK, stupid?")
    elif age_of_user <= 6:
        print("You are a child ;)")
    elif age_of_user <= 17:
        print("You are a schoolboy/schoolgirl")
    elif age_of_user <= 22:
        print("You are a student")
    elif age_of_user <= 30:
        print("You are a youngman or a girl")
    elif age_of_user <= 50:
        print("You are an old human :|")
    else:
        print("Oh, you are so old..(")