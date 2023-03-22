def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

m = 60
n = 24
print(gcd(m, n))  # Output: 6

m < n:  gcd(m,n) = gcd(n,m)
