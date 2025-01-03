import random


NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        quick_pick = generate_quick_pick()
        quick_pick.sort()  # Sort the numbers in ascending order
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:  # Ensure no duplicate numbers
            quick_pick.append(number)
    return quick_pick


main()
