"""
Taxi Simulator Program
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            # Choose a taxi
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")

            try:
                taxi_choice = int(taxi_choice)
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input, please enter a number.")

        elif choice == "d":
            # Drive the taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = input("Drive how far? ")
                try:
                    distance = int(distance)
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    total_bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid input, please enter a number.")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
