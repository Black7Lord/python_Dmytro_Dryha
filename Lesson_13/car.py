from vehicle import Vehicle

class Car(Vehicle):
    pass

if __name__ == '__main__':
    c = Car(
        speed_limit=150,
        wheels_count=4,
        tire_pressure=2.5,
        color='Silver',
        model='Toyota Corolla'
    )

    print(f'{c} проїжджає 10 км по місту за {c.ride(10, 50)} годин')