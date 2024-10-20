FILENAME = 'wimbledon.csv'
CHAMPION_INDEX = 2
CHAMPION_COUNTRY_INDEX = 1

champion_to_count = {}
countries = set()


def main():
    """Read csv file and print the results of winners and their countries"""
    entries = load_data()
    process_entries(entries)
    display_results()


def load_data():
    """Load data into a list of lists"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        return [line.strip().split(",") for line in in_file.readlines()]


def process_entries(entries):
    """Assign keys and values to the dictionary and countries to the set"""
    for entry in entries:
        country = entry[CHAMPION_COUNTRY_INDEX]
        champion = entry[CHAMPION_INDEX]
        countries.add(country)
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1


def display_results():
    """Display the results of champions and their countries"""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
