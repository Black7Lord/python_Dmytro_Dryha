from vehicles import Vehicle

class CarService:
    def __init__(self, name):
        self.name = name

    def maintenance(self, vehicle: Vehicle):
        if not vehicle.construction_needed: # використання декоратора
            print(f'На {self.name} проводиться ТО для {vehicle}')
            for point in vehicle.maintenance_checklist:
                print(point)

            vehicle._maintenance_needed = False
            print(f'ТО для {vehicle} успішно завершено!')
        else:
            print(f'ТЗ {vehicle} не створений!')