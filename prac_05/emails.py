"""
Emails and Names Storage
Estimate: 10 minutes
Actual:   30 minutes
"""


def extract_name_from_email(email):
    """Extract the presumed name from an email address."""
    email_username = email.split('@')[0]
    name = email_username.replace('.', ' ').title()
    return name


def main():
    emails_to_names = {}

    email = input("Email: ").strip()

    while email != "":
        name = extract_name_from_email(email)

        is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_name_correct == 'n':
            name = input("Name: ").strip()
        emails_to_names[email] = name
        email = input("Email: ").strip()

    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


main()
