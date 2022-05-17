from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi services program"""
    bill = 0.00
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets Drive")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ")
    while choice.lower() != "q":
        if choice.lower() == "c":
            display_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice >= len(taxis):
                print("Invalid taxi choice")
                print(f"Bill to date: ${bill:.2f}")
            else:
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill:.2f}")
        elif choice.lower() == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill:.2f}")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                bill += current_taxi.get_fare()
                print(f"Your {current_taxi.name} will cost you ${current_taxi.get_fare():.2f}")
                print(f"Bill to date: ${bill:.2f}")
        else:
            print("Invalid options")
            print(f"Bill to date: ${bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ")
    print("Taxi are now:")
    display_taxi(taxis)


def display_taxi(taxis):
    """Display the list of taxi"""
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


main()