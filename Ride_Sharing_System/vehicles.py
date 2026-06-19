from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vechicle_type, driver_name, distance, rating):
        self.vechicle_type = vechicle_type
        self.driver_name = driver_name
        self.distance = distance
        self._rating = rating

    @property
    def rating(self):
        return self._rating  
        
    @rating.setter
    def rating(self, value):
        if 1 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("Rating must be between 1 and 5")

    @abstractmethod
    def calculate_fare(self):
        pass


class Bike(Vehicle):
    def calculate_fare(self):
        return self.distance * 5


class Car(Vehicle):
    def calculate_fare(self):
        return self.distance * 10


