def euclid_algorithm(m, n):
    count_exec = 0
    if m>=n:
        while n != 0:
            r = m % n
            m = n
            n = r
            count_exec += 1
        return m, count_exec
    else:
        while m != 0:
            r = n % m
            n = m
            m = r
            count_exec += 1
        return n, count_exec

gcd, count = euclid_algorithm(24, 60)
print("GCD: ", gcd)
print("Number of times: ", count)