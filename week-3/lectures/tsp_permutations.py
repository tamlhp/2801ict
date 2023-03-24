import itertools

# Example distances between cities
distances = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

# Function to calculate the total distance of a path through the cities
def path_distance(path):
    total_distance = 0
    for i in range(len(path)-1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]
    return total_distance

# Brute force algorithm to find the shortest path
shortest_distance = float('inf')
shortest_path = []
for path in itertools.permutations(range(len(distances))):
    distance = path_distance(path)
    if distance < shortest_distance:
        shortest_distance = distance
        shortest_path = path

# Print the shortest path and distance
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
