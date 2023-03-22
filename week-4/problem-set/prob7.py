def greedy_change_with_denominations(n, denominations):
    num_coins = 0
    denominations_used = {}
    for denomination in denominations:
        while n >= denomination:
            n -= denomination
            num_coins += 1
            if denomination not in denominations_used:
                denominations_used[denomination] = 1
            else:
                denominations_used[denomination] += 1
    return denominations_used

denominations = [9, 3, 2]
n = 11
denominations_used = greedy_change_with_denominations(n, denominations)
print(denominations_used)
