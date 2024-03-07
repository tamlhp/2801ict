def euclid_algorithm(m, n):
    count_exec = 0
    if m>=n:
        while n != 0:
            r = m % n
            m = n
            n = r
            count_exec += 1
            print(m,n)
        return m, count_exec
    else:
        while m != 0:
            r = n % m
            n = m
            m = r
            count_exec += 1
            print(m,n)
        return n, count_exec

def euclid (m,n, count):
    if m < n: 
        count += 1
        print(m,n)
    if n == 0:
        return m, count
    gcd, subcount = euclid(n, m%n, count)
    count = subcount
    return gcd, count
    
    

# gcd, count = euclid_algorithm(24, 60)
gcd, count = euclid(24, 60, 0)
print("GCD: ", gcd)
print("Number of times: ", count)