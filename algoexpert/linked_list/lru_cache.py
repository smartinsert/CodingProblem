"""
Implement a class for an LRU cache.
1. insert_key_value(key, value)
2. get_value(key)
3. get_most_recent(self)
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None


class LRUCache:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity or 1
        self.current_size = 0
        self.cache = {}
        self.list_of_most_recent = DoublyLinkedList()

    def insert_key_value(self, key, value):
        if key not in self.cache:
            if self.current_size == self.max_capacity:
                self.evict_least_recently_used()
            else:
                self.current_size += 1
            node = Node(key, value)
            self.cache[key] = node
        else:
            self.replace_key(key, value)
        self.update_most_recent_node(self.cache[key])

    def evict_least_recently_used(self):
        self.list_of_most_recent.remove_tail()

    def replace_key(self, key, value):
        if key not in self.cache:
            raise RuntimeError(f'The {key} is not found !')
        node = self.cache[key]
        node.value = value

    def update_most_recent_node(self, node):
        self.list_of_most_recent.set_head_to(node)

    def get_value_from_key(self, key):
        if key not in self.cache:
            return None
        self.update_most_recent_node(self.cache[key])
        return self.cache[key].value

    def get_most_recent_key(self):
        return self.list_of_most_recent.head.key

