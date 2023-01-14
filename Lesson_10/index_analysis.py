import json
import uuid

def create_index(employee_uids: dict, index_key: str) -> dict:
    new_index = dict()
    for uid, employee in employee_uids.items():
        if employee[index_key] in new_index:
            new_index[employee[index_key]].append(uid)
        else:
            new_index[employee[index_key]] = [uid]
    return new_index

if __name__ == '__main__':
    data = json.load(open('hr_department.json', 'r'))
    print(type(data), data)

    employee_ids_index = dict()
    for employee in data['data']:
        _id = f'{employee["name"]}{employee["surname"]}{employee["surname"]}{employee["position"]}{employee["department"]}{employee["salary"]}'
        _uid = uuid.uuid4()
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
        print(f'На посаді {key} працює {len(value)} людей.')

    department_index = create_index(employee_ids_index, 'department')
    for key, value in department_index.items():
        print(f'У відділі {key} працює {len(value)} людей.')

    for uid in department_index['HR']:
        print(employee_ids_index[uid])


# знайти скільки <посада> у <відділ>
# 1) користуватися тільки одним індексом, потім фільтрувати
# 2) set + операція intersection