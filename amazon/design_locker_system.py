# from collections import namedtuple
#
# LockerRange = namedtuple('LockerRange', ['Low', 'High'])
#
#
# class Locker:
#     SMALL_SIZED_LIMIT = 1
#     MEDIUM_SIZED_LIMIT = 3
#     LARGE_SIZE_LIMIT = 5
#
#     def __init__(self, S=10, M=15, L=10, *args, **kwargs):
#         self._max_small_sized_lockers = S
#         self._max_medium_sized_lockers = M
#         self._max_large_sized_lockers = S

from abc import ABC
from enum import Enum


class LockerType(Enum):
    small = 'S'
    medium = 'M'
    large = 'L'


class PackageSize(Enum):
    small = 'S'
    medium = 'M'
    large = 'L'


class Locker(ABC):
    def __init__(self, number, locker_type):
        self.__number = number
        self.__locker_type = locker_type
        self.__is_free = True
        self.__package = None

    def get_number(self):
        return self.__number

    def is_free(self):
        return self.__is_free

    def assign_package(self, package):
        self.__package = package
        self.__is_free = False

    def remove_package(self):
        self.__package = None
        self.__is_free = True


class SmallLocker(Locker):
    def __init__(self, number):
        super().__init__(number, LockerType.small)


class MediumLocker(Locker):
    def __init__(self, number):
        super().__init__(number, LockerType.medium)


class LargeLocker(Locker):
    def __init__(self, number):
        super().__init__(number, LockerType.large)


class Package(ABC):
    def __init__(self, size, *args, **kwargs):
        self.size = size


class SmallPackage(Package):
    def __init__(self):
        super().__init__(PackageSize.small)


class MediumPackage(Package):
    def __init__(self):
        super().__init__(PackageSize.medium)


class LargePackage(Package):
    def __init__(self):
        super().__init__(PackageSize.large)


class AmazonLockerSystem:
    def __init__(self, name):
        self.__small_lockers = {}
        self.__medium_lockers = {}
        self.__large_lockers = {}

    def add_locker(self, locker: Locker):
        switcher  = {
            LockerType.small: self.__small_lockers[locker.get_number()]
        }

