def reverse_stack_with_two_stacks(S):
    R = []
    T = []
    while S:
        R.append(S.pop())
    while R:
        T.append(R.pop())
    while T:
        S.append(T.pop())
    return S

def reverse_stack_with_one_queue(S):
    Q = []
    while S:
        Q.append(S.pop())
    while Q:
        S.append(Q.pop(0))
    return S

def reverse_stack_with_one_stack(S):
    T = []
    while S:
        x = S.pop()
        while T and T[-1] > x:
            S.append(T.pop())
        T.append(x)
    while T:
        S.append(T.pop())
    return S

# example usage of reverse_stack_with_two_stacks
S = [1, 2, 3, 4, 5]
print(reverse_stack_with_two_stacks(S)) # Output: [5, 4, 3, 2, 1]

# example usage of reverse_stack_with_one_queue
S = [1, 2, 3, 4, 5]
print(reverse_stack_with_one_queue(S)) # Output: [5, 4, 3, 2, 1]

# example usage of reverse_stack_with_one_stack
S = [1, 2, 3, 4, 5]
print(reverse_stack_with_one_stack(S)) # Output: [5, 4, 3, 2, 1]
