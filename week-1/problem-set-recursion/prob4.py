# Fibonacci
def rabbit_count(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_count(n-1) + rabbit_count(n-2)

n = 6
print("Rabbit at the year: ", rabbit_count(n)) 