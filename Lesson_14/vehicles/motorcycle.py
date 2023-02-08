from vehicles import Vehicle

class Motorcycle(Vehicle):
    def __str__(self):
        return f"мотоцикл {self.model} кольору {self.color}"

    def __init__(self, model: str, color: str, gasoline_use: float):
        super().__init__(
            speed_limit=250,
            wheels_count=2,
            tire_pressure=2.2,
            color=color,
            model=model,
            maintenance_km=5000
        )
        self.gasoline_use = gasoline_use
        self.maintenance_checklist.append('Міняємо масляні фільтри')

    def ride(self, km: float, local_speed_limit: float) -> float:
        response = super().ride(km, local_speed_limit)
        if response > 0:
            x = self.gasoline_use * km / 100
            print(f'Під час поїздки на {self} було витрачено {x:.1f} літрів бензину')
        return response