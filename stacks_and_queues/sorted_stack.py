import sys


class SortedStack:
    def __init__(self):
        self.original = list()
        self.largest = -1 * sys.maxsize

    def push(self, value):
        self.largest = value if value > self.largest else self.largest
        if not self.original:
            self.original.append(value)
        else:
            last_value = self.original.pop()
            if self.largest > value > last_value:
                self.original.append(last_value)
                self.original.append(value)
            else:
                self.original.append(value)
                self.original.append(last_value)

    def pop(self):
        return self.largest

    def peek(self):
        return self.largest

    def is_empty(self):
        return not self.original

    def sorted_stack(self):
        self.original.append(self.largest)
        return self.original


if __name__ == '__main__':
    s = SortedStack()
    s.push(6)
    s.push(3)
    s.push(9)
    s.push(1)
    print(s.sorted_stack())