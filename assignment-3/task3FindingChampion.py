# Define the directed graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': [],
    'D': ['A', 'C', 'E'],
    'E': ['F'],
    'F': ['G'],
    'G': ['E'],  # Nodes E, F, and G form a cycle.
}

def bfs(start):
    """
    Performs a simple Breadth-First Search (BFS) starting from 'start'.
    Returns a set of all nodes reachable from 'start'.
    """
    visited = {start}      # Starts with the starting node marked as visited.
    queue = [start]        # Uses a list as a queue with the starting node.
    
    # Loops until there are no more nodes to visit.
    while queue:
        current = queue.pop(0)
        # Visits each neighbor of the current node.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def find_champions():
    """
    A champion is a node that can reach every other node.
    We run BFS from each node and check if it visits all nodes.
    """
    champions = []
    total_nodes = len(graph)
    
    # Checks each node in the graph.
    for node in graph:
        if len(bfs(node)) == total_nodes:
            champions.append(node)
    return champions

# Run the algorithm and print the result.
champions = find_champions()
print("Champions in the graph:", champions)
