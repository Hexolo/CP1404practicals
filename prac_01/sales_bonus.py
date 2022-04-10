"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SALES_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
sales_list = []
while sales >= 0:
    if sales >= SALES_THRESHOLD:
        sales_bonus = sales * 0.15
        sales_list.append(sales_bonus)
        sales = float(input("Enter sales: $"))
    elif sales < SALES_THRESHOLD:
        sales_bonus = sales * 0.10
        sales_list.append(sales_bonus)
        sales = float(input("Enter sales: $"))
for i in sales_list:
    print("Sales bonus: ${}".format(i))
