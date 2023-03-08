def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_val = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_val else max_val

numbers = [5, 10, 3, 8, 1]
print(find_max(numbers))