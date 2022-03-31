def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
