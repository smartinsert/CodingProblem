class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + "->", end='')
            temp = temp.next
        if temp is None:
            print('None')
        print()