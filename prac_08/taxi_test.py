from prac_08.taxi import Taxi


def main():
    """Demo testing taxi class"""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print(taxi.get_fare())
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())

main()
