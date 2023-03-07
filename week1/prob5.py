def min_distance(arr):
    arr.sort()
    dmin = float('inf')
    for i in range(1, len(arr)):
        d = abs(arr[i] - arr[i-1])
        if d < dmin:
            dmin = d
    return dmin

arr = [2, 4, 8, 3, 10]
print(min_distance(arr))