import random
LINE = 6

def main():
    """Display lines of number"""
    numbers = []
    quick_pick = int(input("How many quick picks? "))
    for i in range(1, quick_pick+1):
        while len(numbers) != LINE:
            numbers.append(random.randint(1, 45))
            check_number(numbers)
        for number in numbers:
            print(number, end=" ")
        print()


def check_number(numbers):
    



main()