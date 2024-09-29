total_price = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
number_of_items = int(input("Number of items: "))


while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(1, number_of_items + 1):
    price = float(input("Price of items: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    discount_price = total_price - (total_price * DISCOUNT_RATE)
else:
    discount_price = total_price

print(f"Total price for {number_of_items} items is ${discount_price: .2f}")
