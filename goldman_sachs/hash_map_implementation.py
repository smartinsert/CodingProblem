"""
The hash map will be implemented using lists and bucket chaining where each hash value slot will point to
linked list of key and values
"""


class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_element = None


"""
This hash table will contain hash entries
"""


class HashTable:
    def __init__(self):
        # Size of the table
        self.slots = 10
        # Current number of elements in the hash table
        self.size = 0
        # Number of buckets per slot
        self.bucket = [None] * self.slots
        # Threshold to resize
        self.threshold = 0.6

    @property
    def get_size(self):
        return self.size

    @property
    def is_empty(self):
        return self.size == 0

    def get_index(self, key) -> int:
        hash_code = hash(key)
        return hash_code % self.slots

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for i in range(len(self.bucket)):
            head = self.bucket[i]  # HashEntry(key, value)
            while head:
                new_index = self.get_index(head.key)
                # If the slot in the new bucket is empty, initialize that spot with the HashEntry
                if not new_bucket[new_index]:
                    new_bucket[new_index] = HashEntry(key=head.key, value=head.value)
                else:
                    node = new_bucket[new_index]
                    while node:
                        if node.key == head.key:
                            node.value = head.value
                            node = None
                        elif not node.next:
                            node.next_element = HashEntry(key=head.key, value=head.value)
                            node = None
                        else:
                            node = node.next_element
                head = head.next_element
        self.bucket = new_bucket
        self.slots = new_slots

    # O(1)
    def insert(self, key, value):
        # Find the index of the key
        b_index = self.get_index(key=key)
        if not self.bucket[b_index]:
            self.bucket[b_index] = HashEntry(key=key, value=value)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head:
                if head.key == key:
                    head.value = value
                    break
                elif not head.next_element:
                    head.next_element = HashEntry(key=key, value=value)
                    self.size += 1
                    break
                head = head.next_element
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    # O(1)
    def search(self, key):
        # Find the index of the key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while head:
            if head.key == key:
                return head.value
            head = head.next_element
        return None

    def delete(self, key):
        # Find the index of the key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If the key exists in first slot
        if head.key == key:
            self.bucket[b_index] = head.next_element
            self.size -= 1
            return
        prev = None
        while head:
            if head.key == key:
                prev.next_element = head.next_element
                self.size -= 1
                return
            prev = head
            head = head.next_element


if __name__ == '__main__':
    ht = HashTable()
    ht.insert(2, "London")
    ht.insert(7, "Paris")
    ht.insert(8, "Cairo")
    print("size:", ht.get_size)
    ht.delete(2)
    print("size:", ht.get_size)
    print(ht.search(2))
