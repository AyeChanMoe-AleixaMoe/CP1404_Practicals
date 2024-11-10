"""Video 1."""
from pygments.lexer import default

# class Product:
#     def __init__(self, name = "", price = 0.0, is_on_sale = False):
#         self.name = name
#         self.price = price
#         self.is_on_sale = is_on_sale
#     def __str__(self):
#         if self.is_on_sale:
#             on_sale_string = "(on_sale)"
#         else:
#             on_sale_string = ""
#         return f"{self.name}, ${self.price: .2f} {on_sale_string}"
#     def __repr__(self):
#         return str(self)
#     def put_on_sale(self, discount_percent):
#         """Put product on sale by discount percentage as decimal."""
#         self.price *= (1 - discount_percent)
#         self.is_on_sale = True
# p = Product("Phone", 340, False)
# print(p)
# print(p.name, "....")
# p.put_on_sale(0.1)
# print(p)
#
# products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
# on_sale_products = [product for product in products if product.is_on_sale]
# # print(on_sale_products)
#
# for thing in products:
#     print(thing)

"""Video 2."""

# NA

"""Video 3."""

"""Standard Class Methods(Template)"""


# class HelloWorld(App):  # class HelloWorld = Class(new type) , (App) = new class is a specialised version of Kivy's App class (inheritance)
#     def build(self):    # Method (function)
#         self.root = Widget() # self = reference to this instance
#         return self.root
#
# HelloWorld().run() # HelloWorld() = create new object of type HelloWorld, .run() = call method "run" of new object (kivy defines this method)

"""Video 5 (Extras)."""

class User:
    def __init__(self, name="Ben", number_of_tacos = 5, score = 0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score
    def give_tacos(self, other_user):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += 1
        else:
            print("No tacos left to give!")
    def __str__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"
    def __repr__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"

# user = User()
# print(user)

class TacoBattle:
    def __init__(self):
        self.members = []
    def add_member(self, user):
        self.members.remove(user)
    def get_members(self, user):
        for user in self.members:
            if user == self.members:
                return user
    def get_leader(self, user):
        return max(self.members, key=user: user.score, default = None)













