class Vehicle:
    def __init__(self, speed_limit: int, wheels_count: int, tire_pressure: float, color: str, model: str):
        self.speed_limit = speed_limit
        self.wheels = wheels_count
        self.tire_pressure = tire_pressure
        self.color = color
        self.model = model
        self.km_passed = float()
        self.construction_needed = True
        self.maintenance_needed = False

        self.construct()

    def __str__(self):
        return f"транспортний засіб {self.model} кольору {self.color}"

    def construct(self):
        print(f'На заводі зробили {self}')
        self.construction_needed = False
        self.maintenance_needed = False

    def ride(self, km: float, local_speed_limit: float) -> float:
        if self.construction_needed:
            print(f'{self} не готовий до переміщення. Треба створити на заводі')
            return -1
        if self.maintenance_needed:
            print(f'{self} потребує ремонту')
            return -1
        actual_speed = min(local_speed_limit, self.speed_limit)
        return round(km / actual_speed, 2)

    def maintenance(self):
        pass