for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a

for i in range(0, 101, 10):
    print(i, end=' ')

# b

for i in range(1, 21, -1):
    print(i, end=' ')

# c

numbers = int(input("Enter the number of stars: "))

stars = "*" * numbers

print(stars, end=' ')

# d

for i in range(numbers+1):
    print(i*"*")

print()
