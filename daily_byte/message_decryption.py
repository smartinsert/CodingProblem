"""
 Given a message that is encoded using the following encryption method…

A -> 1
B -> 2
C -> 3
...
Z -> 26
Return the total number of ways it can be decoded.
Note: ‘0’ has no mapping and a character following a ‘0’ also has no mapping (i.e. “03”)


Ex: Given the following message…

message = "23", return 2.
The message can be decrypted as "BC" (i.e. 2 -> B, 3 -> C)
The message can also be decrypted as "W" (i.e. 23 -> W)
Ex: Given the following message…

message = "1234", return 3.
"""


def total_ways_to_decode(message: str) -> int:
    if not message or (len(message) == 1 and int(message[0]) == 0):
        return 0
    # alpha_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    #                    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'E': 5,
    #                    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,}
    return count_ways(message, 0, len(message))


def total_ways_to_decode_memo(message: str) -> int:
    if not message or (len(message) == 1 and int(message[0]) == 0):
        return 0
    # alpha_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    #                    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'E': 5,
    #                    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,}
    return count_ways_memo(message, 0, len(message), {})


def count_ways(message: str, start_idx: int, message_length: int):
    if start_idx == message_length:
        return 1
    ways = 0
    if 0 < int(message[start_idx]) < 10:
        ways += count_ways(message, start_idx+1, message_length)
    if start_idx < message_length - 1 and 10 <= int(message[start_idx:start_idx+2]) <= 26:
        ways += count_ways(message, start_idx+2, message_length)
    return ways


def count_ways_memo(message: str, start_idx: int, message_length: int, cache: {}):
    if start_idx == message_length:
        return 1
    if start_idx in cache:
        return cache[start_idx]
    ways = 0
    if 0 < int(message[start_idx]) < 10:
        ways += count_ways(message, start_idx+1, message_length)
    if start_idx < message_length - 1 and 10 <= int(message[start_idx:start_idx+2]) <= 26:
        ways += count_ways(message, start_idx+2, message_length)
    cache[start_idx] = ways
    return ways


# print(total_ways_to_decode('23'))
# print(total_ways_to_decode('1234'))
print(total_ways_to_decode('1234545345345365476467657456456456456456456456465456'))
print(total_ways_to_decode_memo('1234545345345365476467657456456456456456456456465456'))


