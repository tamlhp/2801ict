def find_min_max(arr, low, high):
    if low == high:
        return (arr[low], arr[low])
    elif high == low + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))
    else:
        mid = (low + high) // 2
        (min1, max1) = find_min_max(arr, low, mid)
        (min2, max2) = find_min_max(arr, mid+1, high)
        return (min(min1, min2), max(max1, max2))

# Example usage
arr = [3, 7, 1, 8, 2, 5]
n = len(arr)
(minimum, maximum) = find_min_max(arr, 0, n-1)

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)