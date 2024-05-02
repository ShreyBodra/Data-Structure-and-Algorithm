# The given code is for 0,1 knapsack problem
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    # Calculate value to weight ratio for each item
    value_weight_ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    # Sort items based on value to weight ratio in descending order
    value_weight_ratio.sort(reverse=True)

    total_value = 0
    remaining_capacity = capacity
    selected_items = []

    for ratio, value, weight in value_weight_ratio:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
            selected_items.append((value, weight, 1))  # Fraction taken = 1
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += fraction * value
            selected_items.append((value, weight, fraction))
            break  # No more capacity left

    return total_value, selected_items


# Example usage:
costs = [60, 100, 120]
item_weights = [10, 20, 30]
bag_capacity = 50
max_value, selected_items = fractional_knapsack(costs, item_weights, bag_capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
