from vehicles import Vehicle

class CarService:
    def __init__(self, name):
        self.name = name

    def maintenance(self, vehicle: Vehicle):
        if not vehicle._construction_needed:
            print(f'На {self.name} проводиться ТО для {vehicle}')
            for point in vehicle.maintenance_checklist:
                print(point)

            vehicle._maintenance_needed = False
            vehicle._km_passed_after_mt = 0.0
            print(f'ТО для {vehicle} успішно завершено!')
        else:
            print(f'ТЗ {vehicle} не створений!')