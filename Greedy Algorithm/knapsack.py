# The given code is for 0,1 knapsack problem
def knapsack(values, weights, capacity):
    n = len(values)

    # Calculate value to weight ratio for each item
    value_weight_ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]

    # Sort items based on value to weight ratio in descending order
    value_weight_ratio.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for ratio, value, weight in value_weight_ratio:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
            selected_items.append((value, weight))
        else:
            # If adding the current item exceeds capacity, break the loop
            break

    return total_value, selected_items


# Example usage:
costs = [60, 100, 120]
item_weights = [10, 20, 30]
bag_capacity = 50
max_value, selected_items = knapsack(costs, item_weights, bag_capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
