
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class StackWithMin:
    def __init__(self):
        self.primary = list()
        self.auxillary = list()

    def push(self, value):
        if not self.primary and not self.auxillary:
            self.primary.append(value)
            self.auxillary.append(value)
        else:
            self.primary.append(value)
            y = self.auxillary.pop()
            self.auxillary.append(y)
            if value > y:
                self.auxillary.append(y)
            else:
                self.auxillary.append(value)

    def pop(self):
        if self.auxillary:
            self.auxillary.pop()
        if self.primary:
            return self.primary.pop()

    def min(self):
        if self.auxillary:
            return self.auxillary.pop()


if __name__ == '__main__':
    stack_with_min = StackWithMin()
    stack_with_min.push(7)
    stack_with_min.push(3)
    stack_with_min.push(10)
    stack_with_min.push(1)
    stack_with_min.push(13)
    print(stack_with_min.min())
    print(stack_with_min.pop())
    print(stack_with_min.min())