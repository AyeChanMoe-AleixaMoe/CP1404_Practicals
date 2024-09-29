# total = 0
# count = 0
#
# age = int(input("Enter the age: "))
#
# while age >= 0:
#     total += age
#     count += 1
#     age = int(input("Enter the age: "))
#
# print(total)
# print(total / count)

"""
get number of gifts
get number of students
display number of gifts // number of students
display number of gift % number of students
"""

# number_of_gifts = int(input("Number of gifts: "))
# number_of_students = int(input("Number of students: "))
#
# print(number_of_gifts // number_of_students)
# print(number_of_gifts % number_of_students)

# SG_GST = 0.09
# item_price = float(input("Enter the item price: "))
# gst_confirmation = input("Answer if your item include tax or not. Enter Yes or No").strip().upper()
#
# if gst_confirmation == "YES":
#     final_price = (item_price * SG_GST) + item_price
#     print(f"Final price is {final_price:.2f}")
# else:
#     print(f"Final price is {item_price:.2f}")

# number = int(input("Enter a number: "))
# count = 0
#
# while number > count:
#     count += 1
#     print(count)

# number = int(input("Enter a number: "))
#
# for i in range(1, number + 1):
#     print(i)

# SECRET_NUMBER = 8
#
# user_input = int(input("Guess the secret number(1-10): "))
#
# while user_input < 1 or user_input > 10:
#     print("Invalid input")
#     user_input = int(input("Guess the secret number(1-10): "))
#
# while user_input != SECRET_NUMBER:
#     print("Wrong number. Please try again!")
#     user_input = int(input("Guess the secret number(1-10): "))
#
# print("Correct Number! Horray!!!")

# user_name = input("Enter your name: ").upper()
#
# while user_name == "":
#     print("Invalid name!")
#     user_name = input("Enter your name: ").upper()
#
# user_salary = float(input("Enter your salary: "))
#
# while user_salary < 0:
#     print("Invalid salary!")
#     user_salary = float(input("Enter your salary: "))
#
# print(f"{user_name} earns ${user_salary}")

# ages = []
# number_of_ages = int(input("How many ages do you want to input?: "))
#
# for i in range(1, number_of_ages + 1):
#     input_ages = int(input(f"Enter {i} age: "))
#     ages.append(input_ages)
#
# total = sum(ages)
# average = sum(ages) / len(ages)
#
# print(f"The total is {total} and the average is {average}")

# total = 0
# count = 0
#
# number_of_people = int(input("Enter the number of people: "))
#
# for i in range(1, number_of_people + 1):
#     age = int(input(f"Enter age for person {i}: "))
#     total += age
#     count += 1
#
# print(f"The total is {total}")
# print(f"The average is {(total / count):.2f}.")

# count = 0
# total = 0
# age = int(input("Enter an age: "))
#
# while age != -1:
#     age = int(input("Enter an age: "))
#     count += 1
#     total += age
#
# print(f"The total age is {total}")
# print(f"The average age is {(total / count):.2f}")

# for i in range(1,4):
#     for j in range(2, 10, 3):
#         print(i, "-", j + 1)  "Guess the output"


