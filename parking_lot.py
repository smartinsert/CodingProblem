from abc import ABCMeta, abstractmethod
from enum import Enum


class Colors(Enum):
    red = 'red'
    blue = 'blue'

    def __str__(self):
        return self.value

class ParkingSize(Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'


class Vehicle:
    __metaclass__ = ABCMeta

    def __init__(self, license_number: str, color: Enum, required_parking_size: Enum):
        self.license_number = license_number
        self.color = color
        self.required_parking_size = required_parking_size

    @property
    def get_license_number(self):
        return self.license_number

    @property
    def parking_lot_size(self):
        return self.required_parking_size

    @abstractmethod
    def park(self):
        return NotImplementedError

    @abstractmethod
    def remove(self):
        return NotImplementedError


class Car(Vehicle):

    def __init__(self, license_number, color, required_parking_size):
        super().__init__(license_number, color, required_parking_size)

    def park(self):
        pass

    def remove(self):
        pass

