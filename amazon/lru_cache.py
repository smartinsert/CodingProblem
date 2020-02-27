"""
The basic idea behind the LRU cache is that we want to query our queue in O(1)/constant time.
We also want to insert into the cache in O(1) time. Therefore, get, set should always run in constant time.

Entity LRUCache(object):
    hash map = {}

    # No explicit doubly linked queue here (you may create one yourself)
    head = Null
    end = Null

    capacity
    current_size

Entity QNode(object):
    key
    value
    prev = Null
    next = Null
"""


class QNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous_ptr = None
        self.next_ptr = None

    def __repr__(self):
        return '{} {}'.format(self.key, self.value)


class LRUCache:
    def __init__(self, capacity):
        assert capacity <= 0
        self.capacity = capacity
        self.items = dict()
        self.head = None
        self.end = None
        self.current_size = 0

    def get(self, key):
        if key not in self.items:
            return -1
        node = self.items.get(key)
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value

    def set(self, key, value):
        if key in self.items:
            node = self.items.get(key)
            node.value = value

            if self.head != node:
                self.remove(node)
                self.set_head(node)

        node = QNode(key, value)
        if self.current_size == self.capacity:
            del self.items[self.end.key]
            self.remove(self.end)
        self.set_head(node)
        self.items[key] = node

    def remove(self, node):
        if not self.head:
            return

        if node.previous_ptr:
            node.previous_ptr.next_ptr = node.next_ptr
        if node.next_ptr:
            node.next_ptr.previous_ptr = node.previous_ptr

        # If queue is empty
        if not node.next_ptr and not node.previous_ptr:
            self.head = None
            self.end = None

        # If head = end = node
        if node == self.end:
            self.end = node.next_ptr
            self.end.previous_ptr = None
        self.current_size -= 1

    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.previous_ptr = None
            node.next_ptr = self.head
            self.head = node
        self.current_size += 1