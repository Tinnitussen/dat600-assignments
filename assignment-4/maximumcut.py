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

# Creates a problem to maximize the flow from S to t.
max_flow = pulp.LpProblem("MaxFlow", pulp.LpMaximize)

# This variable represents how much water flows through that connection.
flow = {(i, j): pulp.LpVariable(f"flow_{i}_{j}", lowBound=0, upBound=cap)
        for (i, j, cap) in arcs}

# The objective is to maximize the total flow coming out of S.
max_flow += pulp.lpSum([flow[(i, j)] for (i, j, cap) in arcs if i == 'S'])

# For every node except S and t, the total water flowing in must equal total water flowing out.
for node in nodes:
    if node not in ['S', 't']:
        inflow = pulp.lpSum([flow[(i, j)] for (i, j, cap) in arcs if j == node])
        outflow = pulp.lpSum([flow[(i, j)] for (i, j, cap) in arcs if i == node])
        max_flow += (inflow == outflow)

# Solves the maximum flow problem.
max_flow.solve()

# Displays the results.
print("Maximum Flow:", pulp.value(max_flow.objective))
print("Flow on each edge:")
for (i, j, cap) in arcs:
    print(f"  {i} -> {j}: {flow[(i, j)].varValue}")
