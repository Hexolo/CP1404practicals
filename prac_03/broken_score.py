import random

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}\t", determine_grade(random_score))


def determine_grade(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
