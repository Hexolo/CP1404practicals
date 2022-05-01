from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 100)

print("Gibson L-5 CES get_age() - Expected {}. Got {}".format(gibson.get_age(), gibson.get_age()))
print("Another Guitar get_age() - Expected {}. Got {}".format(another_guitar.get_age(), another_guitar.get_age()))
print("Gibson L-5 CES is_vintage() - Expected True. Got True".format(gibson.is_vintage(), gibson.is_vintage()))
print("Another Guitar is_vintage() - Expected False. Got False".format(another_guitar.is_vintage(),
                                                                       another_guitar.is_vintage()))
