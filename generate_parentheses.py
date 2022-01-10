"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


def generate_parentheses(n: int) -> []:
    if not n:
        return []
    return start_generating(n - 1, n, '(', [])


def start_generating(open: int, close: int, output: str, result: []) -> []:
    if open == 0 and close == 0:
        result.append(output)
    if open != 0:
        start_generating(open - 1, close, output + '(', result)
    if close > open:
        start_generating(open, close - 1, output + ')', result)
    return result


print(generate_parentheses(3))
