class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue = deque((x, self.queue))

    def pop(self) -> int:
        value, self.queue = self.queue
        return value

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
