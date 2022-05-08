from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name}({year}) : ${cost} added.")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name}({year}) : ${cost} added.")
        name = input("Name: ")

    for i, guitar in enumerate(guitars):
        print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{guitar.is_vintage()}")




main()
