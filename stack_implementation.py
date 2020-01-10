class ThreeStacks:
    def __init__(self, size):
        self.size = size
        self.lst = [None] * 3 * size
        self.top = [0, 0, 0]

    def push(self, data, stack_number):
        if 3 > stack_number >= 0:
            self.lst[self._absolute_top_of_stack(stack_number)] = data
            self.top[stack_number] += 1

    def _absolute_top_of_stack(self, stack_number):
        return stack_number * self.size + self.top[stack_number]

    def pop(self, stack_number):
        if 3 > stack_number >= 0:
            temp = self.lst[self._absolute_top_of_stack(stack_number)]
            self.lst[self._absolute_top_of_stack(stack_number)] = None
            self.top[stack_number] -= 1
            return temp

    def size(self, stack_number):
        return self.top[stack_number]


if __name__ == '__main__':
    three_stacks = ThreeStacks(5)
    three_stacks.push(3, 2)