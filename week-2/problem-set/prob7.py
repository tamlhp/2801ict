def sort_stack(S):
    T = []
    while S:
        x = S.pop()
        while T and T[-1] < x:
            S.append(T.pop())
        T.append(x)
    while T:
        S.append(T.pop())
    return S

S = [1, 3, 2, 5, 4]
print(sort_stack(S)) # Output: [1, 2, 3, 4, 5]
