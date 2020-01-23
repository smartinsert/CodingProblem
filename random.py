# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


def backspace_compare(str1, str2):
    idx_1 = len(str1) - 1
    idx_2 = len(str2) - 1
    while idx_1 >=0 or idx_2 >= 0:
        idx1 = get_next_valid_character_index(str1, idx_1)
        idx2 = get_next_valid_character_index(str2, idx_2)

        if idx_1 < 0 and idx_2 < 0:
            return True

        if idx_1 < 0 or idx_2 < 0:
            return False

        if str1[idx1] != str2[idx2]:
            return False

        idx_1 -= 1
        idx_2 -= 1
    return True


def get_next_valid_character_index(string, index):
    backspace_counter = 0
    while index >= 0:
        if string[index] == '#':
            backspace_counter += 1
        elif backspace_counter > 0:
            backspace_counter -= 1
        else:
            break
        index -= 1
    return index
