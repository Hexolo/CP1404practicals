class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{}({}): ${} added.".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return "(Vintage)"
        else:
            return ""
