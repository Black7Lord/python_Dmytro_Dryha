import time

from vehicles import Car
from vehicles import Motorcycle
from vehicles import Bicycle
from car_service import car_service
import random

if __name__ == '__main__':
    vehicle_park = [
        Car(
            color='Silver',
            model='Toyota Corolla',
            gasoline_use=8
        ),
        Car(
            color='Black',
            model='Mitsubishi Outlander',
            gasoline_use=15
        ),
        Motorcycle(
            color='Red',
            model='Pagani',
            gasoline_use=2
        ),
        Bicycle(
            color='White',
            model='Author',
        )
    ]

    my_car_service = car_service.CarService('СТО')

    speed_limit = [50, 90, 140]
    while True:
        v = random.choice(vehicle_park)
        distance = random.randint(100, 1000)
        ride_time = v.ride(distance, random.choice(speed_limit))
        if ride_time > 0:
            print(f'Їдемо на {v} дистанцію {distance}')
        else:
            my_car_service.maintenance(v)
        time.sleep(1)