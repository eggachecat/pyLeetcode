class Queue:
    def __init__(self):
        self.queue = []

    def enter(self, value):
        self.queue.append(value)

    def delete(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        value = self.queue.pop(0)
        return value

    def is_empty(self):
        return len(self.queue) <= 0
