# Example maze represented as a 2D array of 1s and 0s
maze = [[1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

# Function to find a path through the maze using backtracking
def find_path(maze, start, end, path=[]):
    # Add the starting position to the path
    path.append(start)
    # If we have reached the end, return the path
    if start == end:
        return path
    # Get the neighbors of the current position
    neighbors = []
    row, col = start
    if row > 0 and maze[row-1][col] == 1:
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == 1:
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] == 1:
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == 1:
        neighbors.append((row, col+1))
    # Recursively try each neighbor
    for neighbor in neighbors:
        if neighbor not in path:
            new_path = find_path(maze, neighbor, end, path)
            if new_path:
                return new_path
    # If no path was found, remove the current position from the path
    path.pop()

# Find a path through the maze from (0, 0) to (4, 4)
start = (0, 0)
end = (4, 4)
path = find_path(maze, start, end)

# Print the path
if path:
    print("Path found:", path)
else:
    print("No path found.")
