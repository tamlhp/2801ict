def find_largest_position(arr, left, right):
    if left == right:
        return left
    else:
        mid = (left + right) // 2
        left_max_position = find_largest_position(arr, left, mid)
        right_max_position = find_largest_position(arr, mid + 1, right)
        if arr[left_max_position] >= arr[right_max_position]:
            return left_max_position
        else:
            return right_max_position

arr = [3, 5, 4, 6, 2]
largest_position = find_largest_position(arr, 0, len(arr)-1)
print("The largest element in the array is at position", largest_position)
