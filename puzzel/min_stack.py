import sys


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.get_min(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def get_min(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize


minStack = MinStack()
print(minStack.stack)
print(minStack.push(-2))
print(minStack.stack)
print(minStack.push(0))
print(minStack.stack)
print(minStack.push(-3))
print(minStack.stack)
print(minStack.get_min())
print(minStack.stack)
print(minStack.pop())
print(minStack.stack)
print(minStack.top())
print(minStack.stack)
print(minStack.get_min())
print(minStack.stack)
