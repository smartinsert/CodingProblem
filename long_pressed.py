def is_long_typed(name, typed):
    if not name and typed:
        return False
    if not typed and name:
        return False
    if len(name) > len(typed):
        return False
    current_name_idx, current_typed_idx = 0, 0

    while current_name_idx < len(name) and current_typed_idx < len(typed):
        if name[current_name_idx] != typed[current_typed_idx]:
            return False
        next_name_index, next_typed_index = current_name_idx + 1, current_typed_idx + 1
        while next_name_index < len(name) and name[current_name_idx] == name[next_name_index]:
            next_name_index += 1
        while next_typed_index < len(typed) and typed[current_typed_idx] == typed[next_typed_index]:
            next_typed_index += 1
        if next_name_index - current_name_idx > next_typed_index - current_typed_idx:
            return False
        current_name_idx, current_typed_idx = next_name_index, next_typed_index
    return current_name_idx >= len(name) and current_typed_idx >= len(typed)


print(is_long_typed('alex', 'aaleex'))