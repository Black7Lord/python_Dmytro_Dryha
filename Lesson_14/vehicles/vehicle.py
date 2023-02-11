class Vehicle:
    def __init__(self, speed_limit: int, wheels_count: int, tire_pressure: float,
                 maintenance_km: float, color: str, model: str):
        """
        Транспортний засіб. Відповідає за властивості та поведінку ТЗ
        :param speed_limit:
        :param wheels_count:
        :param tire_pressure:
        :param km_passed_after_mt:
        :param color:
        :param model:
        """
        self.speed_limit = speed_limit
        self.wheels = wheels_count
        self.tire_pressure = tire_pressure
        self.color = color
        self.model = model

        # public - доступно всім
        # _protected - доступно лише спадкоємцям - краще не змінювати без повної впевненості
        # __private - лише для самого класу
        self._km_passed_after_mt = float() #0.0
        self.maintenance_needed_km = maintenance_km
        self._construction_needed = True
        self._maintenance_needed = False

        self.maintenance_checklist = [
            f'Підкачуємо шини {self.tire_pressure}'
        ]

        self.construct()

    # getters and setters - методи для отримання та встановлення захищеного поля
    @property # getter
    def construction_needed(self):
        return self._construction_needed

    @property # getter
    def maintenance_needed(self):
        return self._maintenance_needed
    @maintenance_needed.setter # setter
    def maintenance_needed(self, new_value: bool):
        self._maintenance_needed = new_value
        if not new_value:
            self._km_passed_after_mt = 0.0

    # службовий метод. Викликається неявно
    def __str__(self):
        return f"транспортний засіб {self.model} кольору {self.color}"

    def construct(self):
        """
        Створення ТЗ
        """
        print(f'На заводі зробили {self}')
        self._construction_needed = False
        self._maintenance_needed = False

    def ride(self, km: float, local_speed_limit: float) -> float:
        """
        Ізда ТЗ
        :param km:
        :param local_speed_limit:
        :return:
        """
        if self._construction_needed:
            print(f'{self} не готовий до переміщення. Треба створити на заводі')
            return -1
        if self._maintenance_needed:
            print(f'{self} потребує ремонту')
            return -1
        actual_speed = min(local_speed_limit, self.speed_limit)
        self._km_passed_after_mt += km
        if self._km_passed_after_mt > self.maintenance_needed_km:
            self._maintenance_needed = True
            print(f'ТЗ проїхало {self._km_passed_after_mt} км після останнього ТО')
        return round(km / actual_speed, 2)


