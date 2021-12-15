"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".
Example 2:

Input: s = "1*"
Output: 18
Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
Example 3:

Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
"""


def decode_ways_ii(s: str) -> int:
    if not s or (len(s) == 1 and int(s[0]) == 0):
        return 0
    if len(s) == 1 and s[0] == '*':
        return 9
    return count_ways(s, 0, len(s)) - 1


def count_ways(s: str, start: int, length: int) -> int:
    if start == length:
        return 1
    ways = 0
    if s[start] == '*':
        for i in range(1, 10):
            s = s[:start] + str(i) + s[start + 1:]
            ways += count_ways(s, 0, len(s))
    if s[start] != '*' and 0 < int(s[start]) < 10:
        ways += count_ways(s, start + 1, length)
    if '*' not in s[start: start + 2] and start < length - 1 and 10 <= int(s[start: start + 2]) <= 26:
        ways += count_ways(s, start + 2, length)
    return ways


def num_encodings(s: str) -> int:
    dp = [1, 0, 0]
    MOD = 10**9+7
    for c in s:
        tmp = [0, 0, 0]
        if c == '*':
            tmp[0] = dp[0]*9 + dp[1]*9 + dp[2]*6
            tmp[1] = dp[0]
            tmp[2] = dp[0]
        else:
            tmp[0] = (c > '0') * dp[0] + dp[1] + (c <= '6')*dp[2]
            tmp[1] = (c == '1') * dp[0]
            tmp[2] = (c == '2') * dp[0]
        dp = [i % MOD for i in tmp]
    return dp[0]

# print(decode_ways_ii('1*'))
# print(decode_ways_ii('2*'))
# print(num_encodings('**'))
print(num_encodings('123*4'))

