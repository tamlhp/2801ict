import matplotlib.pyplot as plt
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        # recursively sort left and right subarrays
        merge_sort(left_arr)
        merge_sort(right_arr)
        # merge the sorted subarrays
        merge(arr, left_arr, right_arr)

def merge(arr, left_arr, right_arr):
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        # visualize the current state of the array
        plt.bar(range(len(arr)), arr)
        plt.show(block=False)
        plt.pause(0.1)

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        # visualize the current state of the array
        plt.bar(range(len(arr)), arr)
        plt.show(block=False)
        plt.pause(0.1)

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
        # visualize the current state of the array
        plt.bar(range(len(arr)), arr)
        plt.show(block=False)
        plt.pause(0.1)

# generate random data to sort
data = [random.randint(0, 50) for _ in range(15)]
# visualize the initial state
plt.bar(range(len(data)), data)
plt.show(block=False)
plt.pause(1)

# sort the data and visualize each step
merge_sort(data)

# visualize the final sorted state
plt.bar(range(len(data)), data)
plt.show()
