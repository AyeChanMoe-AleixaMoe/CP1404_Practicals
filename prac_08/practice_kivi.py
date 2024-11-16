from kivy.app import App
from kivy.app import Builder
class BoxLayout(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

BoxLayout().run()
