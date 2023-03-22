def alternating_disks(disks):
    n = len(disks) // 2
    while True:
        swapped = False
        for i in range(n*2 - 1):
            if disks[i] < disks[i+1]:
                disks[i], disks[i+1] = disks[i+1], disks[i]
                swapped = True
        if not swapped:
            break
    return disks

disks = ["D", "L", "D", "L", "D", "L", "D", "L"]
solved_disks = alternating_disks(disks)
print(solved_disks)