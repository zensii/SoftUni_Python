from typing import List

class Stack:

    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
            self.data.append(str(element))

    def pop(self):
        return self.data.pop()

    def top(self):
        top = self.data[-1]
        return top

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        result = f"[{', '.join(reversed(self.data))}]"
        return result
