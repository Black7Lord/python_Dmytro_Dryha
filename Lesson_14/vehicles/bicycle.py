from vehicles import Vehicle

class Bicycle(Vehicle):
    def __str__(self):
        return f"велосипед {self.model} кольору {self.color}"

    def __init__(self, model: str, color: str):
        super().__init__(
            speed_limit=30,
            wheels_count=2,
            tire_pressure=2.0,
            color=color,
            model=model,
            maintenance_km=1000
        )
        self.maintenance_checklist.append('Чищемо ланцюг')

    def ride(self, km: float, local_speed_limit: float) -> float:
        if km > 300:
            print(f'Велосипедист не зможе проїхати {km} km!')
            return -1
        return super().ride(km, local_speed_limit)