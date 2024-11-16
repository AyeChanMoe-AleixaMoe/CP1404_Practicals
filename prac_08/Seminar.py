# from kivy.app import App
# from kivy.app import Widget
# class HelloWorld(App):
#     def build(self):
#         self.root = Widget()
#         return self.root
# HelloWorld().run()

# from kivy.app import App
# from kivy.app import Widget
# from kivy.lang import Builder
#
#
# class HelloWorld(App):
#     def build(self):
#         self.title = 'Hello World!'
#         self.root = Builder.load_file('widget.kv')
# HelloWorld().run()

# from kivy.app import App
# from kivy.app import Widget
# from kivy.lang import Builder
# import random


# class ButtonEventDemo(App):
#     def build(self):
#         self.title = 'Button Event Demo'
#         self.root = Builder.load_file('button_event.kv')
#         return self.root
#     def handle_button_press(self, button):
#         print(f'app: + {self}')
#         print(str(button) + ' say "ouch!"')
#         print(f"Button text: '{button.text}', pos: {button.pos}")
#     def handle_release(self, button):
#         print("Hello")
#     def handle_release_dont(self):
#         print("Released the don't button")
# ButtonEventDemo().run()

# class IDDemo(App):
#     def build(self):
#         self.title = 'Demoing the id attribute'
#         self.root = Builder.load_file('id_demo.kv')
#         return self.root
#     def handle_button_press(self):
#         if random.randint(1,10) <= 5:
#             self.root.ids.my_label.text = 'ouch!'
#         else:
#             self.root.ids.my_label.text = 'stop that!'
#
# IDDemo().run()


from kivy.app import App
from kivy.app import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty

class MVCDemo(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        self.title = 'Simple MVC Demo'
        self.root = Builder.load_file('mvc.kv')
        self.message = "Type in the field & press 'Enter'."
        return self.root
    def handle_update(self):
        """Handle changes to the text input by updating the model"""
        self.message = self.root.ids.user_input.text

MVCDemo().run()