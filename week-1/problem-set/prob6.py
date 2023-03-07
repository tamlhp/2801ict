def comparison_counting_sort(A):
    n = len(A)
    Count = [0] * n
    S = [0] * n
    
    for i in range(n):
        for j in range(i+1, n):
            if A[i] < A[j]:
                Count[j] += 1
            else:
                Count[i] += 1
                
    for i in range(n):
        S[Count[i]] = A[i]
        
    return S

A = [60,  35,  81,  98,  14,  47]
S = comparison_counting_sort(A)
print(S)  # Output: [1, 2, 5, 5, 6, 9]
