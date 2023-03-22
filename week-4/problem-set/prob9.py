def max_coin_row(coins):
    n = len(coins)
    tm = [0] * (n + 1)
    tm[1] = coins[0]
    for i in range(2, n+1):
        tm[i] = max(tm[i-1], coins[i-1] + tm[i-2])
    
    return tm[n]

coins = [5, 1, 2, 10, 6]
print(max_coin_row(coins)) # Output: 15