def delete_element(arr, i):
    # Swap ith element with last element
    arr[i], arr[-1] = arr[-1], arr[i]
    
    # Pop last element to delete ith element
    arr.pop()
    
    return arr

class SortedArray:
    def __init__(self, arr):
        self.arr = arr
        self.deleted = [False] * len(arr)

    def delete(self, i):
        self.deleted[i] = True

    def search(self, x):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.deleted[mid]:
                if mid == left or self.arr[right] < x:
                    right = mid - 1
                else:
                    left = mid + 1
            elif self.arr[mid] < x:
                left = mid + 1
            elif self.arr[mid] > x:
                right = mid - 1
            else:
                return mid
        return -1

    def __len__(self):
        return sum(1 for i in range(len(self.arr)) if not self.deleted[i])

    def __getitem__(self, i):
        if self.deleted[i]:
            raise IndexError('Index out of range')
        else:
            return self.arr[i]

    def __iter__(self):
        for i in range(len(self.arr)):
            if not self.deleted[i]:
                yield self.arr[i]

arr = [1, 2, 3, 4, 5]
i = 2  # Index of element to delete (i.e., the value 3)
sorted_arr = SortedArray(arr)
print(delete_element(arr.copy(), i))

sorted_arr.delete(i)
print(len(sorted_arr))
print(list(sorted_arr))
print(sorted_arr.search(4))