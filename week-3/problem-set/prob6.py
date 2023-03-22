import numpy as np

def count_recursion(coins, n, sum):
    if sum == 0:
        return 1

    if sum < 0 or n <= 0:
        return 0

    without_current_coin = count_recursion(coins, n - 1, sum)
    with_current_coin = count_recursion(coins, n, sum - coins[n-1])
    return without_current_coin + with_current_coin

def count_dynamic_programming(coins, n, sum):
    table = np.zeros((n, sum+1), dtype=int)
    table[:, 0] = 1

    for i in range(n):
        for j in range(1, sum+1):
            if coins[i] > j:
                table[i][j] = table[i-1][j]
            else:
                # Count of solutions excluding
                x = table[i-1][j]
                # Count of solutions including coins[j]
                y = table[i][j-coins[i]]
                table[i][j] = x + y
    return table[-1][-1]


# Driver program to test above function
coins = [1, 2, 3]
n = len(coins)
sum = 4
print(count_recursion(coins, n, sum))
print(count_dynamic_programming(coins, n, sum))
