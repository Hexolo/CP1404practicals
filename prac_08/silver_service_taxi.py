from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = 0
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, fuel={} {}km on current fare, ${:.2f}/km plus flagfall of ${}".format(self.name, self.fuel,
                                                                                          self.current_fare_distance,
                                                                                          self.price_per_km,
                                                                                          self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    # def start_fare(self):
    #     """Begin a new fare."""
    #     self.current_fare_distance = 0
    #
    # def drive(self, distance):
    #     """Drive like parent Car but calculate fare distance as well."""
    #     distance_driven = super().drive(distance)
    #     self.current_fare_distance += distance_driven
    #     return distance_driven
