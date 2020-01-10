class QueueWithTwoStacks:
    def __init__(self):
        self.stack_1 = list()
        self.stack_2 = list()

    def push(self, value):
        self.stack_1.append(value)

    def pop(self):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


if __name__ == '__main__':
    q = QueueWithTwoStacks()
    q.push(3)

    print(q.pop())
    
    q.push(1)
    q.push(7)
    q.push(4)

    print(q.pop())