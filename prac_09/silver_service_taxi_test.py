"""
CP1404/CP5632 Practical
Test the SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    # Create a SilverServiceTaxi with fanciness of 2
    hummer = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    hummer.start_fare()
    hummer.drive(18)

    # Print the taxi's details and fare
    print(hummer)
    fare = hummer.get_fare()
    print(f"Fare: ${fare:.2f}")

    # Assert that the fare is correct (for testing purposes)
    assert abs(fare - 48.80) < 0.01, f"Expected $48.80 but got ${fare:.2f}"


if __name__ == "__main__":
    main()
