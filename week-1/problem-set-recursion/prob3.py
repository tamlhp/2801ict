def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

def reverse_inplace(s):
    if len(s) <= 1:
        return
    n = len(s)
    s[n-1], s[0] = s[0], s[n-1]
    reverse_inplace(s[1:n-1])

s = "hello world"
print(reverse_string(s))
print(reverse_inplace(s))