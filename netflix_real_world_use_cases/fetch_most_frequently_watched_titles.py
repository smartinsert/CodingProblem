"""
When the data structure is at capacity, a newly inserted item will replace the least frequently accessed item.
In the case of a tie, the least recently accessed item should be replaced.
"""
import collections


class LinkedListNode:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev, node.next = None, None


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_nodes = collections.defaultdict(LinkedList)

    def get(self, key):
        if key not in self.key_to_node:
            return None
        temp_node = self.key_to_node[key]
        self.key_to_node[key] = LinkedListNode(key, temp_node.value, temp_node.freq)
        self.freq_to_nodes[temp_node.freq].delete(temp_node)
        if not self.freq_to_nodes[self.key_to_node[key].freq].head:
            del self.freq_to_nodes[self.key_to_node[key].freq]
            if self.min_freq == self.key_to_node[key].freq:
                self.min_freq += 1
        self.key_to_node[key].freq += 1
        self.freq_to_nodes[self.key_to_node[key].freq].append(self.key_to_node[key])
        return self.key_to_node[key].value

    def set(self, key, value):
        if self.get(key) is not None:
            self.key_to_node[key].value = value
            return

        if self.size == self.capacity:
            del self.key_to_node[self.freq_to_nodes[self.min_freq]]
            self.freq_to_nodes[self.min_freq].delete(self.freq_to_nodes[self.min_freq].head)
            if not self.freq_to_nodes[self.min_freq].head:
                del self.freq_to_nodes[self.min_freq]
            self.size -= 1

        self.min_freq = 1
        new_node = LinkedListNode(key, value, self.min_freq)
        self.key_to_node[key] = new_node
        self.freq_to_nodes[self.key_to_node[key].freq].append(self.key_to_node[key])
        self.size += 1



