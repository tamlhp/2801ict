def is_max_heap(H):
    n = len(H) - 1  # The number of nodes in the heap (excluding the first element, H[0])

    # Iterate through the parent nodes
    for i in range(1, n//2 + 1):
        left_child = 2 * i
        right_child = 2 * i + 1

        # Check if the parent node follows the max-heap property with respect to its child nodes
        if left_child <= n and H[i] < H[left_child]:
            return False
        if right_child <= n and H[i] < H[right_child]:
            return False

    # If all parent nodes follow the max-heap property, the array is a max-heap
    return True

# Example 1: A max-heap
heap_example1 = [None, 90, 80, 70, 60, 50, 40, 30, 20, 10]
result1 = is_max_heap(heap_example1)
print("Example 1 is a max-heap:", result1)  # Should print True

# Example 2: Not a max-heap
heap_example2 = [None, 90, 80, 70, 60, 50, 40, 100, 20, 10]
result2 = is_max_heap(heap_example2)
print("Example 2 is a max-heap:", result2)  # Should print False
