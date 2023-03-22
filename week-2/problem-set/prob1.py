class Node:
    def __init__(self, value, index):
        self.value = value
        # self.index = index
        self.next = None
        # self.prev = None


class LinkedList:
    def __init__(self, values):
        self.head = None
        self.tail = None
        self.size = 0

        for value in values:
            self.append(value)

    def append(self, value):
        new_node = Node(value, self.size)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1


# Function to perform binary search on a sorted array
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found


# Function to perform interpolation search on a sorted array
def interpolation_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1  # Target not found


# Function to perform linear search on a sorted linked list
def linear_search(head, target):
    current = head
    
    while current is not None and current.value <= target:
        if current.value == target:
            return current.index
        current = current.next
    
    return -1  # Target not found


# Function to perform skip list search on a sorted linked list
def skip_list_search(head, target):
    current = head
    
    while current is not None and current.value <= target:
        if current.value == target:
            return current.index
        elif current.next is None or current.next.value > target:
            current = current.down
        else:
            current = current.next
    
    return -1  # Target not found


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
linked_list = LinkedList([1, 3, 5, 7, 9, 11, 13, 15, 17])

print(binary_search(arr, 11))  # Output: 5
print(interpolation_search(arr, 11))  # Output: 5
print(linear_search(linked_list.head, 11))  # Output: 5
print(skip_list_search(linked_list.head, 11))  # Output: 5
