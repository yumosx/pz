from typing import Optional

class Stack[T]:
    def __init__(self):
        self._container: list[T] = []
    def __str__(self):
        return str(self._container)
    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._container
    def is_empty(self):
        return self._container == []
    def size(self) -> int:
        return len(self._container)