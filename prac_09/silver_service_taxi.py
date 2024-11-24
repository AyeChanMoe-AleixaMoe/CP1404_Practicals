"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with higher pricing and a flagfall."""

    flagfall = 4.50  # Class variable for additional charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)  # Call the Taxi constructor with name and fuel
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Adjust price_per_km based on fanciness

    def get_fare(self):
        """Calculate the total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
