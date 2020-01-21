

def format_string(starting: list, ending: list, style: list) -> int:
    ordered_pairs = list(zip(starting, ending))
    result = [''] * max(max(starting), max(ending))
    total_operations = 0
    for idx, pair in enumerate(ordered_pairs):
        styling = style[idx]
        current_operations = 0
        for position in range(pair[0], pair[1]):
            if styling not in result[position]:
                result[position] = styling
                current_operations = 2
            else:
                current_operations = 0
        total_operations += current_operations
    return total_operations


if __name__ == '__main__':
    assert format_string([1, 3, 9, 5, 5], [5, 8, 10, 6, 6], ['b', 'i', 'b', 'i', 'u']) == 8
