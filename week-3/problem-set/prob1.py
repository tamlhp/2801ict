def determine_topology(A):
    n = len(A)
    
    # Check for Ring Topology
    is_ring = True
    for i in range(n):
        neighbors = 0
        for j in range(n):
            if A[i][j]:
                neighbors += 1
        if neighbors != 2:
            if i == 0 or i == n-1:
                if neighbors != 1:
                    is_ring = False
            else:
                is_ring = False
    if is_ring:
        return "Ring Topology"
    
    # Check for Star Topology
    is_star = True
    center = -1
    for i in range(n):
        neighbors = 0
        for j in range(n):
            if A[i][j]:
                neighbors += 1
        if neighbors == n-1:
            if center == -1:
                center = i
            else:
                is_star = False
        elif i != center:
            if neighbors != 1:
                is_star = False
    if is_star:
        return "Star Topology"
    
    # Check for Fully Connected Mesh Topology
    is_fully_connected_mesh = True
    for i in range(n):
        for j in range(n):
            if i != j and not A[i][j]:
                is_fully_connected_mesh = False
    if is_fully_connected_mesh:
        return "Fully Connected Mesh Topology"
    
    return "Unknown Topology"

adj_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

topology = determine_topology(adj_matrix)
print(topology)  # Output: Ring Topology

adj_matrix = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

topology = determine_topology(adj_matrix)
print(topology)  # Output: Star Topology

adj_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

topology = determine_topology(adj_matrix)
print(topology)  # Output: Fully Connected Mesh Topology

adj_matrix = [
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
]

topology = determine_topology(adj_matrix)
print(topology)  # Output: Unknown Topology
