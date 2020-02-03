

def longest_common_prefix(S: str):
    lcp = ''
    if not S:
        return lcp
    current = 0
    for character in S[0]:
        for i in range(1, len(S)):
            if current >= len(S[i]) or S[i][current] != character:
                return lcp
        lcp += character
        current += 1
    return lcp


if __name__ == '__main__':
    print(longest_common_prefix(['flower', 'flow', 'flight']))
    print(longest_common_prefix(['dog', 'racecar', 'car']))