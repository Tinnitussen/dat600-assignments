def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0

    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (capacity / weight) * value
            break

    return total_value

# Test Case
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Fractional Knapsack:", fractional_knapsack(weights, values, capacity))
