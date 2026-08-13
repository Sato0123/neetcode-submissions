import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if not self.stack:
            return None
        val = self.stack.pop()
        if not self.stack:
            self.min = math.inf
        elif val == self.min:
            self.min = min(self.stack)
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
