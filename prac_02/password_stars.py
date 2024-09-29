def main():

    MINIMUM_LENGTH = 5
    password = input("Enter a password: ")

    password = get_valid_password(MINIMUM_LENGTH, password)

    print_asterisks(password)


def print_asterisks(password):
    asterisks = "*" * len(password)
    print(asterisks)


def get_valid_password(MINIMUM_LENGTH, password):
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long".format(MINIMUM_LENGTH))
        password = input("Enter a password: ")
    return password


main()