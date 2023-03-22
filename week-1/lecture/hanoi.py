def hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from the source to the auxiliary peg
        hanoi(n-1, source, auxiliary, target)
        
        # Move the largest disk from the source to the target peg
        target.append(source.pop())
        print("Move disk", n, "from", source, "to", target)
        
        # Move the n-1 disks from the auxiliary peg to the target peg
        hanoi(n-1, auxiliary, target, source)
        
# Example usage:
source = [3, 2, 1]
target = []
auxiliary = []
hanoi(len(source), source, target, auxiliary)