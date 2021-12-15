

def backspace_compare(str1, str2):
    if str1 == str2:
        return True
    left_idx, right_idx = len(str1) - 1, len(str2) - 1
    while left_idx >= 0 or right_idx >= 0:
        valid_left_idx = next_valid_character_index(str1, left_idx)
        valid_right_idx = next_valid_character_index(str2, right_idx)
        if str1[valid_left_idx] != str2[valid_right_idx]:
            return False
        if valid_left_idx < 0 and valid_right_idx < 0:
            return True
        if valid_left_idx < 0 or valid_right_idx < 0:
            return False
        left_idx = valid_left_idx - 1
        right_idx = valid_right_idx - 1
    return True


def next_valid_character_index(string: str, index: int) -> int:
    backspace_count = 0
    while index >= 0:
        if string[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index


# print(backspace_compare("xy#z", "xzz#"))
# print(backspace_compare("xy#z", "xyz#"))
print(backspace_compare("xp#", "xyz##"))
