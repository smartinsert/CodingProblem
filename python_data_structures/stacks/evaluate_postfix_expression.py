"""
Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def top(self):
        return self.stack[-1]

    def push(self, element):
        self.stack.append(element)


def evaluate_postfix(postfix_string):
    stack = Stack()
    try:
        for character in postfix_string:
            if character.isdigit():
                stack.push(character)
            else:
                right = stack.pop()
                left = stack.pop()
                result = str(eval(left + character + right))
                stack.push(result)
        return int(float(stack.pop()))
    except:
        return 'Invalid Sequence'


if __name__ == '__main__':
    print(evaluate_postfix("921*-8-4+"))