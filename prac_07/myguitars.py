import csv
from guitar import Guitar

def main():
    guitars =  load_file()
    display_guitars(guitars)

    name = input("Enter a new guitar name or blank to stop: ")
    while name:
        year = int(input("Enter Year: "))
        cost = float(input("Enter Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter a new guitar name or blank to stop: ")

    save_guitars(guitars)


def save_guitars(guitars):
    with open("guitars.csv", "w", newline="") as guitars_file:
        guitars_writer = csv.writer(guitars_file)
        for guitar in guitars:
            guitars_writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost: .2f}")


def load_file():
    guitars = []
    with open("guitars.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars

if __name__ == '__main__':
    main()