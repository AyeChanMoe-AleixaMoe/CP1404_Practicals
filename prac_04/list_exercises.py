# Step 1: Prompt user for 5 numbers and store them in a list
numbers = []

for i in range(5):
    number = float(input(f"Number {i+1}: "))
    numbers.append(number)

# Output the required information
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers):.1f}")

# Step 2: Username security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Enter your username: ")

if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
