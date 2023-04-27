class ChainingHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, value):
        return value % 2

    def insert(self, value):
        index = self.hash_function(value)
        print(index)
        if value not in self.table[index]:
            self.table[index].append(value)
            return True
        else:
            return False

def is_distinct(lst):
    hash_table = ChainingHashTable()
    for elem in lst:
        if not hash_table.insert(elem):
            return False
    return True

# Example usage
lst = [1, 11, 21, 31]
print(is_distinct(lst))  # Output: True