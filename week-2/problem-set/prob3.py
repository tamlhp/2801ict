class PriorityQueueUnsortedArray:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item, priority):
        self.items.append((item, priority))
    
    def dequeue(self):
        if self.is_empty():
            return None
        highest_priority_item = self.items[0]
        for item, priority in self.items:
            if priority > highest_priority_item[1]:
                highest_priority_item = (item, priority)
        self.items.remove(highest_priority_item)
        return highest_priority_item[0]


class PriorityQueueSortedArray:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items = sorted(self.items, key=lambda x: x[1], reverse=True)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()[0]


class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.left = None
        self.right = None
    
class PriorityQueueBinarySearchTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def enqueue(self, item, priority):
        if self.is_empty():
            self.root = Node(item, priority)
        else:
            self._enqueue_helper(item, priority, self.root)
    
    def _enqueue_helper(self, item, priority, node):
        if priority > node.priority:
            if node.left is None:
                node.left = Node(item, priority)
            else:
                self._enqueue_helper(item, priority, node.left)
        else:
            if node.right is None:
                node.right = Node(item, priority)
            else:
                self._enqueue_helper(item, priority, node.right)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self._dequeue_helper(self.root)[0]
    
    def _dequeue_helper(self, node):
        if node.left is None:
            self.root = node.right
            return (node.item, node.priority)
        else:
            item, priority = self._dequeue_helper(node.left)
            if node.left.left is None:
                node.left = node.left.right
            return (item, priority)


# Example usage
pq1 = PriorityQueueUnsortedArray()
pq1.enqueue("Task 1", 3)
pq1.enqueue("Task 2", 1)
pq1.enqueue("Task 3", 2)
print(pq1.dequeue())  # "Task 1"
print(pq1.dequeue())  # "Task 3"
print(pq1.dequeue())  # "Task 2"

pq2 = PriorityQueueSortedArray()
pq2.enqueue("Task 1", 3)
pq2.enqueue("Task 2", 1)
pq2.enqueue("Task 3", 2)
print(pq2.dequeue())  # "Task 1"
print(pq2.dequeue())  # "Task 3"
print(pq2.dequeue())  # "Task 2"

pq3 = PriorityQueueBinarySearchTree()
pq3.enqueue("Task 1", 3)
pq3.enqueue("Task 2", 1)
pq3.enqueue("Task 3", 2)
print(pq3.dequeue())  # "Task 1"
print(pq3.dequeue())  # "Task 3"
print(pq3.dequeue())