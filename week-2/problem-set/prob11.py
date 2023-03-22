def stock_span(prices):
    stk = []
    span = []

    for i in range(len(prices)):
        cur_span = 1
        while stk and prices[stk[-1]] <= prices[i]:
            prev_idx = stk.pop()
            cur_span += span[prev_idx]
        span.append(cur_span)
        stk.append(i)

    return span



import time

start_time = time.time()
# calculateShares(10**12)
# calculateShares(3)
prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))
end_time = time.time()
print(end_time - start_time)

n = 10**12
print(n)
