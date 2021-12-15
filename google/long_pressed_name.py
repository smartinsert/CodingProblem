
def long_pressed(name: str, typed: str) -> bool:
    if not name and typed:
        return False
    if name and not typed:
        return False
    if name == typed:
        return True
    i, j = 0, 0
    while i < len(name) and j < len(typed):
        name_char, typed_char = name[i], typed[j]
        if name_char != typed_char:
            return False
        named_idx, typed_idx = i + 1, j + 1
        while named_idx < len(name) and name[named_idx] == name[i]:
            named_idx += 1
        while typed_idx < len(typed) and typed[typed_idx] == typed[j]:
            typed_idx += 1
        if typed_idx - j < named_idx - i:
            return False
        i, j = named_idx, typed_idx
    return i >= len(name) and j >= len(typed)


print(long_pressed("alex", "aaleex"))
print(long_pressed("saeed", "ssaaedd"))
print(long_pressed("leelee", "lleeelee"))
print(long_pressed("rick", "kric"))
