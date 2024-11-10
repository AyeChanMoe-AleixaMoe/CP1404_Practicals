# class Monitor:
#     """A monitor with model, width, and height."""
#
#     def __init__(self, model, width, height):
#         self.model = model
#         self.width = width
#         self.height = height
#
#     def get_resolution(self):
#         """Return (width, height)."""
#         return self.width, self.height
#
#     def get_total_pixels(self):
#         """Return width * height."""
#         return self.width * self.height

# class Monitor:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def is_equal(self, other):
#         return self.width == other.width and self.height == other.height
#
# monitor1 = Monitor(1920, 1080)
# monitor2 = Monitor(1920, 1080)
# monitor3 = Monitor(1280, 720)
#
# print(monitor1.is_equal(monitor2))  # Expected: True
# print(monitor1.is_equal(monitor3))  # Expected: False

# class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def __eq__(self, other):
# #         if isinstance(other, self.__class__):
# #             return self.name == other.name and self.age == other.age
# #         return False
# #
# # person1 = Person("John", 25)
# # person2 = Person("John", 25)
# # person3 = Person("Bob", 25)
# #
# # print(person1 == person2)
# # print(person1 == person3)
# # print(person1 != person2)

