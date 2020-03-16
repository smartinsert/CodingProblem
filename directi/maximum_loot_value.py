"""
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming
that any fraction of a loot item can be put into his bag.
"""


def get_optimal_value(capacity, weights, values):
    value = 0.
    if capacity == 0:
        return 0
    for i in range(len(weights)):
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            available_weights = min(capacity, weights[max_index])
            value = value + available_weights * values[max_index]/weights[max_index]
            weights[max_index] = weights[max_index] - available_weights
            capacity = capacity - available_weights
    return value


def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(len(weights)):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i]/weights[i]
            index = i
    return index


if __name__ == '__main__':
    print(get_optimal_value(50, [20, 50, 30], [6, 100, 120]))