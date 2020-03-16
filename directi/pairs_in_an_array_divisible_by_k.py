"""
Check if an array can be divided into pairs whose sum is divisible by k.
Input: arr[] = {92, 75, 65, 48, 45, 35}, k = 10
"""

# Use two pointer approach


def is_pairable(array, k):
    mod_k = [0] * k
    for n in array:
        mod_k[n % k] += 1
        mod_k[-n % k] -= 1

        if n % k == -n % k:
            mod_k[n % k] ^= 1

    return not any(mod_k)


if __name__ == '__main__':
    print(is_pairable([92, 75, 65, 48, 45, 35], 10))
    print(is_pairable([92, 73, 66, 48, 44, 37], 10))
    print(is_pairable([92, 73], 10))