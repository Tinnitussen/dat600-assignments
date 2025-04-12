import pulp

# Defines our nodes and the connections (edges) with their capacities.
nodes = ['S', 'V1', 'V2', 'V3', 'V4', 'V5', 't']
arcs = [
    ('S','V1', 14),
    ('S','V2', 25),
    ('V1','V3', 3),
    ('V1','V4', 21),
    ('V2','V3', 13),
    ('V2','V5', 7),
    ('V3','V1', 6),
    ('V3','V5', 15),
    ('V4','t', 20),
    ('V4','V3', 10),
    ('V5','V4', 5),
    ('V5','t', 10)
  
]

# Creates a problem that minimizes the capacity of the cut edges.
problem = pulp.LpProblem("MinimumCut", pulp.LpMinimize)

# For each node, create a binary variable: 0 means the node is with S; 1 means it's with t.
group = {node: pulp.LpVariable(f"group_{node}", cat="Binary") for node in nodes}

# For each edge, create a binary variable that becomes 1 if the edge goes from group 0 (S) to group 1 (t).
cut_edge = {}
for (i, j, capacity) in arcs:
    cut_edge[(i, j)] = pulp.LpVariable(f"cut_{i}_{j}", cat="Binary")
    problem += cut_edge[(i, j)] >= group[j] - group[i]

# Fix the groups for the source and sink.
problem += group['S'] == 0  # S must be in the S group(source).
problem += group['t'] == 1  # t must be in the t group(sink).

# The total cut capacity is the sum of capacities of the crossing edges.
problem += pulp.lpSum([capacity * cut_edge[(i, j)] for (i, j, capacity) in arcs])

# Solves the problem.
problem.solve()

# Displays the results.
print("Minimum Cut Capacity:", pulp.value(problem.objective))
print("Node Assignments:")
for node in nodes:
    print(f"  {node}: Group", int(group[node].varValue))
