import random

LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Display lines of number"""
    numbers = []
    quick_pick = int(input("How many quick picks? "))
    for i in range(quick_pick):
        remove_repeated_number(numbers)
        numbers.sort()
        for number in numbers:
            print(number, end=" ")
        print()
        numbers.clear()


def remove_repeated_number(numbers):
    """Program that check and replace"""
    while len(numbers) != LINE:
        num1 = 0
        num2 = 1
        if len(numbers) != 2:
            numbers.append(random.randint(MINIMUM, MAXIMUM))
        elif numbers[num1] == numbers[num2]:
            numbers.remove(numbers[num2])
        else:
            numbers.append(random.randint(MINIMUM, MAXIMUM))
        num1 += 1
        num2 += 1
    return numbers


main()
