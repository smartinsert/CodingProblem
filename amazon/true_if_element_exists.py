"""
Given a 1D Array. Return True if there exists an element where a[i]+a[j] = 0 && i!=j.

Input : arr = {2,-3,4,1,-6,-4,1}
Output : True

Input : arr = {2,3,4,1,-6,4,1}
Output : False
"""

from typing import List


def element_exists(arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == 0:
                return True
    return False


if __name__ == '__main__':
    print(element_exists([2,-3,4,1,-6,-4,1]))
    print(element_exists([2, 3, 4, 1, -6, 4, 1]))