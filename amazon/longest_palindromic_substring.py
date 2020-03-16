"""
Longest palindromic substring
"""

# Recursive


def number_of_longest_substring_recursive(sequence, i, j):
    if i == j:
        return 1

    if sequence[i] == sequence[j] and i + 1 == j:
        return 2 + number_of_longest_substring_recursive(sequence, i + 1, j - 1)

    return max(number_of_longest_substring_recursive(sequence, i, j-1),
               number_of_longest_substring_recursive(sequence, i + 1, j)
               )


def longest_palindromic_strings(sequence):
    length = len(sequence)
    max_length = 1
    start = 0
    for i in range(1, length):
        # Even length palindrome
        low = i - 1
        high = i
        while low >= 0 and high < length and sequence[low] == sequence[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # Odd length palindrome
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and sequence[low] == sequence[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    return sequence[start: start+max_length]


if __name__ == '__main__':
    sequence = 'aaaabaaa'
    print(number_of_longest_substring_recursive(sequence, 0, len(sequence) - 1))
    print(longest_palindromic_strings(sequence))