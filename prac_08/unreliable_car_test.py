from prac_08.unreliable_car import UnreliableCar



def main():
    """Testing Unreliable Car"""
    car = UnreliableCar("Lexus", 100, 40.67)
    print(car)
    car.drive(40)
    print(car.distance)


main()
