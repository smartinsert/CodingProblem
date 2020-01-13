class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self and self.value) + ',' + str(self and self.next)


class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.top)

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return None
        popped_element = self.top
        self.top = self.top.next
        return popped_element.value


def sort_stack(stack):
    previous = stack.pop()
    current = stack.pop()
    temp = Stack()
    while current:
        if previous < current:
            temp.push(previous)
            previous = current
            current = stack.pop()
        else:
            temp.push(current)
            current = stack.pop()
        if not current and previous:
            temp.push(previous)
    sorted = True
    previous = temp.pop()
    current = temp.pop()
    while current:
        if previous > current:
            stack.push(previous)
            previous = current
            current = temp.pop()
        else:
            stack.push(current)
            current = temp.pop()
            sorted = False
        if not current and previous:
            stack.push(previous)
    if sorted:
        return stack
    else:
        return sort_stack(stack)


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(30)
    s.push(70)
    s.push(40)
    s.push(80)
    s.push(20)
    s.push(90)
    print(sort_stack(s))