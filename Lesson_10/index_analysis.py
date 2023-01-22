import json
from uuid import uuid4

def create_index(employee_uids: dict, index_key: str) -> dict:
    new_index = dict()
    for uid, employee in employee_uids.items():
        if employee[index_key] in new_index:
            new_index[employee[index_key]].append(uid)
        else:
            new_index[employee[index_key]] = [uid]
    return new_index

def positions_in_department_view(
        employee_uids: dict, _department_index: dict,
        _department_name: str, debug: bool = False
) -> dict:
    """
    Функція рахує кількість посад у вказаному відділі.
    У словнику, що повертається, будуть лише ті посади, які є у відділу, а не всі.
    :param _department_name: ім'я відділу
    :param _department_index: індекс відділу
    :param employee_uids: індекс співробітників
    :param debug: прапорець для перевірки коректної роботи
    :return: словник: ключ - посади у відділі, значення - їхня кількість
    """
    #print(f'У відділі {_department_name} працюють:')
    positions_in_department = dict()
    for _uid in _department_index[_department_name]:
        if debug:
            print(employee_uids[_uid])
        employee_position = employee_uids[_uid]['position']
        if employee_position in positions_in_department:
            positions_in_department[employee_position] += 1
        else:
            positions_in_department[employee_position] = 1
    # print(positions_in_department)
    return positions_in_department

if __name__ == '__main__':
    data = json.load(open('hr_department.json', 'r'))
    print('1. ', type(data), data)

    employee_ids_index = dict()
    for employee in data['data']:
        _id = f'{employee["name"]}{employee["surname"]}{employee["surname"]}{employee["position"]}{employee["department"]}{employee["salary"]}'
        _uid = uuid4()
        employee_ids_index[_uid] = employee

    """
            "name": "Will",
            "surname": "Collier",
            "position": "Manager",
            "department": "Production",
            "salary": 2400
    """

    position_index = create_index(employee_ids_index, 'position')
    for key, value in position_index.items():
        print(f'2. На посаді {key} працює {len(value)} людей.')

    department_index = create_index(employee_ids_index, 'department')
    for key, value in department_index.items():
        print(f'3. У відділі {key} працює {len(value)} людей.')

    print('4. У відділі HR працюють:')
    for uid in department_index['HR']:
        print(employee_ids_index[uid])

# знайти скільки <посада> у <відділ>
# 1) користуватися тільки одним індексом, потім фільтрувати кожну групу
# 2) set + операція intersection

    for department_name in department_index.keys():
        print(f'5. У відділі {department_name} працюють такі посади: ', positions_in_department_view(employee_ids_index, department_index, department_name))

    # print(positions_in_department_view(employee_ids_index, department_index, 'Art'))