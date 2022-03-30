"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? if it's a string
2. When will a ZeroDivisionError occur? When a denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes you can check before you do the
division using if and else statement
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    if denominator == 0:
        fraction = 0
    else:
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")