def power_of_two(n):
  if n == 0:
    return 1
  else:
    return 2 * power_of_two(n-1)

print(power_of_two(5))