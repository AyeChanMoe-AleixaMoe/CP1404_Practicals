"""
CP1404/CP5632 Practical
Test the UnreliableCar class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    # Create several UnreliableCar instances with different reliabilities
    high_reliability_car = UnreliableCar("High Reliability", 100, 90)
    low_reliability_car = UnreliableCar("Low Reliability", 100, 20)

    # Try driving each car a few times and print the results
    print(f"{high_reliability_car.name}:")
    for i in range(5):
        distance_driven = high_reliability_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")

    print(f"\n{low_reliability_car.name}:")
    for i in range(5):
        distance_driven = low_reliability_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")


if __name__ == "__main__":
    main()
