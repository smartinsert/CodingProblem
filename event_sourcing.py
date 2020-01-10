import unittest
import attr
import uuid
import typing
from abc import ABCMeta, abstractmethod


class Order:
    def __init__(self, user_id: int, status: str = 'new'):
        self.user_id = user_id
        self.status = status

    def set_status(self, new_status: str):
        if new_status not in ['new', 'paid', 'confirmed', 'shipped']:
            raise ValueError(f'{new_status} is not a correct status')
        self.status = new_status


class OrderCreated:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


class StatusChanged:
    def __init__(self, new_status: str):
        self.new_status = new_status

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


@attr.s(frozen=True)
class OrderCreatedBetter:
    user_id: int = attr.ib()


@attr.s(frozen=True)
class StatusChanged:
    new_status: str = attr.ib()

class OrderES:
    def __init__(self, events: list):
        for event in events:
            self.apply(event)
        self.changes = []

    def apply(self, event):
        if isinstance(event, OrderCreated):
            self.user_id = event.user_id
            self.status = 'new'
        elif isinstance(event, StatusChanged):
            self.status = event.new_status
        else:
            raise ValueError(f'unknown event {event}')

    def set_status(self, new_status: str):
        status_changed = StatusChanged(new_status)
        self.apply(status_changed)
        self.changes.append(status_changed)

    @classmethod
    def create(cls, user_id: int):
        order_created = OrderCreated(user_id)
        instance = cls([order_created])
        instance.changes = [order_created]
        return instance


class OrderAggregateTest(unittest.TestCase):

    def test_should_create_order(self):
        order = OrderES.create(1)
        self.assertEqual(order.changes, [OrderCreated(1)])

    def test_should_emit_set_status_event(self):
        order = OrderES([OrderCreated(user_id=1)])
        order.set_status('confirmed')
        self.assertEqual(order.changes, [StatusChanged('confirmed')])


class Event(object):
    pass


class EventStream(object):
    def __init__(self, events: typing.List[Event], version: int):
        self.events = events
        self.version = version


class EventStore(metaclass=ABCMeta):
    @abstractmethod
    def load_stream(self, aggregate_uuid: uuid.UUID) -> EventStream:
        raise NotImplementedError

    # @abstractmethod
    # def append_to_stream(self, aggre):

if __name__ == '__main__':
    unittest.main()