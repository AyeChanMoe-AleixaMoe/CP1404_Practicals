MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    choice = input("Choose: ").upper()
    score = int(input("Enter score: "))
    while choice != "Q":
        if choice == "G":
            get_valid_score(score)
        elif choice == "P":
            result = get_score_category(score)
            print(result)
        else:
            print_asterisks(score)
        print(MENU)
        choice = input("Choose: ").upper()
    print("Farewell!!")


def print_asterisks(score):
    asterisks = "*" * score
    print(asterisks)


def get_valid_score(score):
    while score >= 100 or score < 0:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))


def get_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"
