# shopping_app.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from product import Product  # Import the Product model

class MainLayout(BoxLayout):
    pass

class ShoppingApp(App):
    # Total price for all selected products
    total_price = NumericProperty(0)

    def build(self):
        # Define the list of products
        self.products = [
            Product("Cheese", 12.50),
            Product("Laptop", 912.95),
            Product("Plant", 4.75),
            Product("Coffee Machine", 2300.00),
            Product("Guitar", 4399.95)
        ]
        return MainLayout()

    def add_to_total(self, price):
        """Add the selected product's price to the total."""
        self.total_price += price

    def reset_total(self):
        """Reset the total price to zero."""
        self.total_price = 0

if __name__ == "__main__":
    ShoppingApp().run()
