import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Example weighted adjacency matrix
adj_matrix = np.array([[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]])

# Convert adjacency matrix to a weighted graph
G = nx.DiGraph(adj_matrix)
# G = nx.from_numpy_matrix(adj_matrix, create_using=nx.DiGraph)

# Define positions for the nodes
pos = nx.spring_layout(G)

# Draw the graph with edge labels
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()
