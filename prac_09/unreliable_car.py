import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it is reliable enough."""
        if random.uniform(0, 100) < self.reliability:
            # If the random number is less than reliability, drive the car
            return super().drive(distance)
        # If the car is unreliable, it drives 0 km
        return 0
