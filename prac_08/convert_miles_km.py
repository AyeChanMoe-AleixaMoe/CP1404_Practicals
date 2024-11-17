from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION_RATE = 1.60934

class ConvertMilesToKm(App):
    message = StringProperty()
    def build(self):
        self.title = "Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root
    def handle_update(self):
        """Handle the conversion of miles to kilometers."""
        try:
            miles = float(self.root.ids.user_input.text)
            kilometer = miles * MILES_TO_KM_CONVERSION_RATE
            self.message = f"{kilometer: .2f} km"
        except ValueError:
            self.root.ids.user_input.text = "0"
            self.handle_update()
    def handle_increment(self, increment):
        """Handle increment or decrement of miles."""
        try:
            miles = float(self.root.ids.user_input.text) if self.root.ids.user_input.text else 0.0
            miles += increment
            self.root.ids.user_input.text = str(miles)
            self.handle_update()
        except ValueError:
            self.root.ids.user_input.text = "0"
            self.handle_update()

ConvertMilesToKm().run()