from vehicles import Vehicle

class Car(Vehicle):

    def __init__(self, model: str, color: str, gasoline_use: float):
        super().__init__(
            speed_limit=150,
            wheels_count=4,
            tire_pressure=2.5,
            color=color,
            model=model,
            maintenance_km=8000
        )
        self.gasoline_use = gasoline_use
        self.maintenance_checklist.append('Мфняємо масляні фільтри')
    def __str__(self):
        return f"автомобіль {self.model} кольору {self.color}"

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Логіка така ж, як у базового класу, але додає кількість витраченого пального
        :param km:
        :param local_speed_limit:
        :return:
        """
        response = super().ride(km, local_speed_limit)
        if response > 0:
            x = self.gasoline_use * km / 100
            print(f'Під час поїздки на {self} було витрачено {x:.1f} літрів бензину')
        return response

if __name__ == '__main__':
    c = Car(
        color='Silver',
        model='Toyota Corolla',
        gasoline_use=8
    )

    print(f'{c} проїжджає 10 км по місту за {c.ride(10, 50)} годин')
    c._maintenance_needed = False

    c.ride(8000, 90)
    c.ride(100, 90)
    c.maintenance()
    print(c.ride(100, 90))
    print(c.ride(100, 90))