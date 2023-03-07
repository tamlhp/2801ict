1. One way to delete the ith element of an array in constant time, without depending on the size n, is to use a technique called "swap and pop". Here's how it works:

Swap the ith element with the last element in the array. This can be done in constant time because the indices of both elements are known.
Pop the last element from the array. This removes the ith element from the array while maintaining its order.

This technique works because it only requires two operations that do not depend on the size of the array. Swapping two elements and popping the last element can both be done in constant time, so this method deletes the ith element in constant time.

2. One way to delete the i-th element of a sorted array without depending on its size n is to use a technique called "lazy deletion".

In lazy deletion, instead of actually removing the i-th element from the array, we mark it as "deleted" using a flag or a sentinel value. This means that the i-th element is still technically in the array, but we treat it as if it doesn't exist when performing any subsequent operations on the array.

To delete the i-th element using lazy deletion, we simply set the flag or sentinel value for that element. Since this operation only involves changing a single element of the array, it takes constant time, independent of the array's size.

When performing operations on the array, such as searching or sorting, we ignore any elements that are marked as deleted. This means that the array appears as if the i-th element has been removed, even though it technically still exists in the array.

Note that lazy deletion can result in wasted memory if a large portion of the array is marked as deleted. In addition, it may require additional bookkeeping to keep track of which elements are marked as deleted. However, if the number of deleted elements is small compared to the size of the array, lazy deletion can be a useful technique for deleting elements in a sorted array without depending on its size.
