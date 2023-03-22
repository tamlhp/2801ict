def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Print the intermediate sorted array
        print(f"Step {i+1}: {arr}")
        
    return arr

# Example usage
arr = [89, 45, 68, 90, 29, 34, 17]
print("Original array: ", arr)
sorted_arr = selection_sort(arr)
print("Sorted array: ", sorted_arr)