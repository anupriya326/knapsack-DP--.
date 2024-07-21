import matplotlib.pyplot as plt
import networkx as nx

# Define the knapsack problem
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
n = len(weights)

# Create a directed graph
G = nx.DiGraph()

# Function to add nodes and edges to the graph for the recursion tree
def add_nodes_edges(capacity, index, path, memo):
    if index == n or capacity == 0:
        return 0
    if (index, capacity) in memo:
        return memo[(index, capacity)]
    
    # Include the item
    if weights[index] <= capacity:
        include = values[index] + add_nodes_edges(capacity - weights[index], index + 1, path + [(index, capacity)], memo)
    else:
        include = 0
    # Exclude the item
    exclude = add_nodes_edges(capacity, index + 1, path + [(index, capacity)], memo)
    
    result = max(include, exclude)
    memo[(index, capacity)] = result
    
    # Add nodes and edges
    if path:
        parent = path[-1]
        G.add_edge(parent, (index, capacity), color='red' if (index, capacity) in memo else 'green')
    G.add_node((index, capacity), value=result)
    
    return result

# Initialize memoization dictionary
memo = {}
# Start the recursion
max_value = add_nodes_edges(capacity, 0, [], memo)

# Set node colors based on memoization
node_colors = []
for node in G.nodes():
    if node in memo:
        node_colors.append('#66FF66')  # green for memoized
    else:
        node_colors.append('#FF6666')  # red for non-memoized

# Draw the graph
pos = nx.spring_layout(G)
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]

plt.figure(figsize=(12, 8))
nx.draw(G, pos, edge_color=colors, node_color=node_colors, with_labels=True, node_size=3000, font_size=10, font_weight='bold', font_family='Verdana')
plt.title('Knapsack DP Recursion Tree')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Define the knapsack problem
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
n = len(weights)

# Create the memoization table
memo_table = np.full((n + 1, capacity + 1), -1)

# Fill the memoization table
for i in range(n + 1):
    for w in range(capacity + 1):
        if i == 0 or w == 0:
            memo_table[i][w] = 0
        elif weights[i - 1] <= w:
            memo_table[i][w] = max(values[i - 1] + memo_table[i - 1][w - weights[i - 1]], memo_table[i - 1][w])
        else:
            memo_table[i][w] = memo_table[i - 1][w]

# Create a plot of the memoization table
fig, ax = plt.subplots(figsize=(10, 6))
ax.matshow(memo_table, cmap=plt.cm.Blues)

for i in range(n + 1):
    for j in range(capacity + 1):
        c = memo_table[i, j]
        ax.text(j, i, str(c), va='center', ha='center')

plt.title('Knapsack DP Memoization Table')
plt.xlabel('Capacity')
plt.ylabel('Items')
plt.show()
