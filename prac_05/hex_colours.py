NAME_TO_CODE = {"Absolute Zero": "#0048ba",
                "Acid Green": "#b0bf1a", "Alizarin Crimson": "#e32636",
                "Amber": "#ffbf00", "Aqua": "#00ffff", "BabyBlue": "#89cff0",
                "Baby Pink": "#f4c2c2", "Bitter Lemon": "#cae00d", "Bitter Lime": "#bfff00",
                "Black": "#000000"}

colour = input("Enter colour name: ").title()
while colour != "":
    if colour in NAME_TO_CODE:
        print(colour, "is", NAME_TO_CODE[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ").title()