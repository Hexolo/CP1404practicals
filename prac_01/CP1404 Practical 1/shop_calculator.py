item_prices = []
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(1, items + 1):
    price = float(input("Price of item: "))
    item_prices.append(price)
print("Total price of 3 items is ${:.2f}".format(sum(item_prices)))
