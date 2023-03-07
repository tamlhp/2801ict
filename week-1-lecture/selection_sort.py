import matplotlib.pyplot as plt
import numpy as np

def selection_sort(arr):
    """
    Sorts an array in ascending order using selection sort.
    """
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title('Selection Sort')
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Update the visualization
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        fig.canvas.draw()
        plt.pause(1)
        
    return arr

# Example usage
arr = np.random.randint(1, 50, size=20)
print(f"Unsorted array: {arr}")
sorted_arr = selection_sort(arr)
print(f"Sorted array: {sorted_arr}")