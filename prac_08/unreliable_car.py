from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.distance = 0

    def __str__(self):
        """Return a string representation of a UnreliableCar object."""
        return "{}, fuel={}, reliability={}".format(self.name, self.fuel,
                                                    self.reliability)

    def drive(self, distance):
        """Drive like parent Car but with chance to not able to drive"""
        number = random.uniform(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
            self.distance += distance_driven
            return distance_driven
        else:
            print("Oh No! Something's Wrong")
            distance_driven = 0
            return distance_driven
