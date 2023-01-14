# HR dep data
import json
from random import randint, choice
"""
name, surname, position, date_starteed, ipn, department, salary
{
}
"""

NUM_EMPLOYEES = 20
SALARY_LOWER_BOUND = 300
SALARY_UPPER_BOUND = 4000

def full_for():
    # regular for-loop
    with open('actor_names.txt') as f:
        list_of_names = list()
        for line in f.readlines():
            if line.count(' ') == 1:
                list_of_names.append(line.strip())
        print(list_of_names)

def full_comp():
    # comprehension
    with open('actor_names.txt') as f:
        list_of_names = [line.strip() for line in f.readlines() if line.count(' ') == 1]
        print(list_of_names)

def split_for():
    # розділити на ім'я та прізвище for-loop
    with open('actor_names.txt') as f:
        list_of_firstnames = list()
        list_of_lastnames = list()
        for line in f.readlines():
            line = line.split()
            if len(line) == 2:
                list_of_firstnames.append(line[0])
                list_of_lastnames.append(line[1])
        return list_of_firstnames

def split_for_2():
    # розділити на ім'я та прізвище for-loop
    with open('actor_names.txt') as f:
        list_of_firstnames = list()
        list_of_lastnames = list()
        for line in f.readlines():
            line = line.split()
            if len(line) == 2:
                list_of_firstnames.append(line[0])
                list_of_lastnames.append(line[1])
        return list_of_lastnames

def split_comp():
    # розділити на ім'я та прізвище comprehension
    # неефективно! - багато циклів
    with open('actor_names.txt') as f:
        list_of_names = [line.split() for line in f.readlines() if line.count(' ') == 1]
        list_of_firstnames = [x[0] for x in list_of_names]
        list_of_lastnames = [x[1] for x in list_of_names]
        print(list_of_firstnames)
        print(list_of_lastnames)

    """
    with open('actor_names.txt') as f:
        list_of_firstnames = [line.split()[0] for line in f.readlines() if line.count(' ') == 1]
    with open('actor_names.txt') as f:
        list_of_lastnames = [line.split()[1] for line in f.readlines() if line.count(' ') == 1]
    """



if __name__ == '__main__':


    position = ['Engineer', 'Manager', 'Administrator', 'Director', 'Employee']
    department = ['Security', 'Art', 'Economics', 'HR', 'Production', 'Research']

    list_of_firstnames = split_for()
    list_of_lastnames = split_for_2()

    first_names = set(list_of_firstnames)
    last_names = set(list_of_lastnames)


    json_object = list()
    for i in range(NUM_EMPLOYEES):
        d = {
            "name": choice(list(first_names)),
            "surname": choice(list(last_names)),
            "position": choice(position),
            "department": choice(department),
            "salary": randint(SALARY_LOWER_BOUND / 100, SALARY_UPPER_BOUND / 100) * 100
        }
        json_object.append(d)
    json.dump({"data":json_object}, open('hr_department.json', 'w'), indent=4)