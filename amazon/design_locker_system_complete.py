from collections import namedtuple

LockerRange = namedtuple('LockerRange', ['low', 'high'])


class LockerSystem:
    SMALL_SIZE_LIMIT = 1
    MEDIUM_SIZE_LIMIT = 3
    LARGE_SIZE_LIMIT = 5

    def __init__(self, small_lockers=10, medium_lockers=20, large_lockers=10, *args, **kwargs):
        self.small_locker_range = LockerRange(low=0, high=small_lockers-1)
        self.medium_locker_range = LockerRange(low=0, high=medium_lockers - 1)
        self.large_locker_range = LockerRange(low=0, high=large_lockers - 1)

        # Declare capacity counter
        self.small_locker_counter = 0
        self.medium_locker_counter = small_lockers
        self.large_locker_counter = small_lockers + medium_lockers

        self.order_id_to_locker_id = {}

    def __get_next_locker_id(self, package_size):
        locker_id = -1
        if package_size < LockerSystem.SMALL_SIZE_LIMIT and self.small_locker_counter <= self.small_locker_range.high:
            locker_id = self.small_locker_counter
            self.small_locker_counter += 1
        if package_size < LockerSystem.MEDIUM_SIZE_LIMIT and self.medium_locker_counter <= self.medium_locker_range.high:
            locker_id = self.medium_locker_counter
            self.medium_locker_counter += 1
        if package_size < LockerSystem.LARGE_SIZE_LIMIT and self.large_locker_counter <= self.large_locker_range.high:
            locker_id = self.large_locker_counter
            self.large_locker_counter += 1
        return locker_id

    def set_locker(self, order_id, package_size):
        locker_id = self.__get_next_locker_id(package_size)
        if locker_id > 0:
            if order_id not in self.order_id_to_locker_id:
                self.order_id_to_locker_id[order_id] = locker_id
            else:
                raise RuntimeError(f'{order_id} already exists')
        raise RuntimeError(f'Cannot allocate locker to {order_id}')

    def get_locker_number(self, order_id):
        if order_id in self.order_id_to_locker_id:
            return self.order_id_to_locker_id[order_id]
        return -1





