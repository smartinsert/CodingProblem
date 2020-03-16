"""
Implement Hash Table using List as the underlying data structure and chaining along with resizing as the
hash collision handling technique.
It will be an n*m size hash table where there will be n keys and m slots per bucket. Each slot holds a key/value pair
"""


class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_element = None

    def __repr__(self):
        return f'({self.key}, {self.value}) -> {self.next_element}'


class HashTable:
    def __init__(self):
        self.slots = 10  # number of keys
        self.size = 0  # current size
        self.bucket = [HashEntry(0, 0)] * self.slots  # bucket for a key
        self.threshold = 0.6

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash function
    def get_index(self, key):
        hash_code = hash(key)
        return hash_code % self.slots

    def resize(self):
        new_slots = 2 * self.slots
        new_bucket = [HashEntry(0, 0)] * new_slots
        # rehash all items to new slots
        for i in range(len(self.bucket)):
            head = self.bucket[i]
            while head is not None:
                new_index = self.get_index(head.key)
                # If the new_index of the new_bucket is empty, put a hash entry there
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                # Else traverse the linked list to the end and add the HashEntry there
                # If the node is not empty, it will have some HashEntry
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key == head.key:
                            node.value = head.value
                            break
                        elif node.next_element is None:
                            node.next_element = HashEntry(head.key, head.value)
                            break
                        node = node.next_element
                head = head.next_element
        self.bucket = new_bucket
        self.slots = new_slots

    # insert the HashEntry and check if resize is necessary
    def insert(self, key, value):
        bucket_index = self.get_index(key)
        if self.bucket[bucket_index] is None:
            self.bucket[bucket_index] = HashEntry(key, value)
            self.size += 1
        else:
            node = self.bucket[bucket_index]
            while node is not None:
                if node.key == key:
                    node.value = value
                    break
                elif node.next_element is not None:
                    node.next_element = HashEntry(key, value)
                    break
                node = node.next_element
            self.size += 1
        if self.get_size() > self.threshold * self.slots:
            self.resize()

    def search(self, key):
        bucket_index = self.get_index(key)
        head = self.bucket[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next_element
        return None

    def delete(self, key):
        bucket_index = self.get_index(key)
        head = self.bucket[bucket_index]
        # Find the key
        if head.key == key:
            self.bucket[bucket_index] = head.next_element
            self.size -= 1
            return self
        prev = None
        while head is not None:
            if head.key == key:
                prev.next_element = head.next_element
                self.size -=1
                return
            prev = head
            head = head.next_element
        return f'{key} not found'


