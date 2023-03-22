def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = True
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = False
        if swapped:
            print("Swapped. Break!")
            break
    return array

my_list = [4, 2, 8, 3, 1, 9, 6, 5, 7]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_list = bubble_sort(my_list)
print(sorted_list)
