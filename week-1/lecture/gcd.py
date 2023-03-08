def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 60
b = 24
print(gcd(a, b))  # Output: 6
