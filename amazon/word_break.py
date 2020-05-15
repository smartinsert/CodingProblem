"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for length in range(1, len(s) + 1):
        for i in range(length):
            if dp[i] and s[i:length] in wordDict:
                dp[length] = True
                break
    return dp[len(s)]


def word_break(string, word_dict):
    words = set()
    for word in word_dict:
        words.add(word)
    return dfs(string, words)


def dfs(string, words):
    if string == '':
        return True

    for i in range(1, len(string)+1):
        if string[:i] in words and dfs(string[i:], words):
            return True
    return False


if __name__ == '__main__':
    print(wordBreak('code', ['c', 'od', 'e', 'xy']))
    print(word_break('code', ['c', 'od', 'e', 'xy']))
