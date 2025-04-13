import pulp

model = pulp.LpProblem("Manufacture_profit_maximization", pulp.LpMaximize)

x = pulp.LpVariable("x", lowBound=10, cat='Integer')
y = pulp.LpVariable("y", lowBound=0, cat='Integer')

model += 505 * x + 770 * y, "Objective_function"
model += 15 * x + 20 * y <= 2400, "x_time_limit"
model += 20 * x + 30 * y <= 2100, "y_time_limit"

status = model.solve()

print("Task 1: Manufacturing optimization")
print(f"Problem status: {pulp.LpStatus[status]}")

if status == pulp.LpStatusOptimal:
    optimal_x = x.varValue
    optimal_y = y.varValue

    profit = pulp.value(model.objective)
    profit = profit / 3

    print(f"Optimal production plan:")
    print(f"Units of X = {optimal_x:.2f}")
    print(f"Units of Y = {optimal_y:.2f}")
    print(f"Maximum Weekly Profit = {profit:.2f}")
else:
    print("No optimal solution found.")