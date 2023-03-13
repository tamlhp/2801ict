class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("Queue is empty")
        return self.dequeue_stack.pop()

    def is_empty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue()) # Output: 1
q.enqueue(4)
print(q.dequeue()) # Output: 2
print(q.dequeue()) # Output: 3
print(q.dequeue()) # Output: 4
print(q.is_empty()) # Output: True
