from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the list of names (data or model)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Load the kv file and create the widgets dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create a Label for each name in the list."""
        for name in self.names:
            # Create a new Label widget with the name as text
            temp_label = Label(text=name, font_size=24)
            # Add the Label to the BoxLayout with id 'main'
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
