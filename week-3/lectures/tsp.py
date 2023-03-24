import numpy as np

# Example distances between cities
distances = np.array([[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]])

# Function to find the shortest path through the cities using backtracking
def tsp_backtrack(distances, current_city, visited, path, current_distance, shortest_path, shortest_distance):
    # Add the current city to the path and mark it as visited
    path.append(current_city)
    visited[current_city] = True
    # If we have visited all cities, update the shortest path if necessary
    if len(path) == len(distances):
        if current_distance + distances[current_city, 0] < shortest_distance[0]:
            shortest_path[:] = path[:]
            shortest_distance[0] = current_distance + distances[current_city, 0]
    else:
        # Try each unvisited neighbor recursively
        for neighbor in range(len(distances)):
            if not visited[neighbor]:
                tsp_backtrack(distances, neighbor, visited, path, current_distance+distances[current_city, neighbor], shortest_path, shortest_distance)
    # Remove the current city from the path and mark it as unvisited
    path.pop()
    visited[current_city] = False

# Initialize variables and call the backtracking function
start_city = 0
visited = np.zeros(len(distances), dtype=bool)
path = []
shortest_path = []
shortest_distance = [float('inf')]
tsp_backtrack(distances, start_city, visited, path, 0, shortest_path, shortest_distance)

# Print the shortest path and distance
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
