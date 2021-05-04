class MonotonicQueue:
    def __init__(self) -> None:
        self.data = []

    def push(self, x: int) -> None:
        while self.data and self.data[-1] < x:
            self.data.pop()
        self.data.append(x)

    def pop(self, x: int) -> None:
        if self.data and self.data[0] == x:
            self.data.pop(0)

    def max(self) -> int:
        return self.data[0] if self.data else -1
