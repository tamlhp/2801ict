def tower_of_hanoi(n, src, dest, aux):
    stack = []
    stack.append((n, src, dest, aux))

    while stack:
        n, src, dest, aux = stack.pop()
        if n == 1:
            print(f"Move disk from {src} to {dest}")
        else:
            stack.append((n-1, aux, dest, src))
            stack.append((1, src, dest, aux))
            stack.append((n-1, src, aux, dest))

# Example usage:
tower_of_hanoi(3, 'A', 'C', 'B')
