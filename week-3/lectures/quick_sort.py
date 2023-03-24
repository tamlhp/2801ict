import matplotlib.pyplot as plt
import random

def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # visualize the swap
            plt.bar(range(len(arr)), arr)
            plt.show(block=False)
            plt.pause(0.1)
    arr[i+1], arr[right] = arr[right], arr[i+1]
    # visualize the swap
    plt.bar(range(len(arr)), arr)
    plt.show(block=False)
    plt.pause(0.1)
    return i+1

# generate random data to sort
data = [random.randint(0, 50) for _ in range(15)]
# visualize the initial state
plt.bar(range(len(data)), data)
plt.show(block=False)
plt.pause(1)

# sort the data and visualize each step
quick_sort(data, 0, len(data) - 1)

# visualize the final sorted state
plt.bar(range(len(data)), data)
plt.show()
