"""
Find all occurrences of pattern in a string
"""
import time
from typing import List, Dict, Tuple
from collections import defaultdict


def all_occurrences(text: str, patterns: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    pattern_to_position = defaultdict() # O(K)
    for pattern in patterns:
        word_length = len(pattern)
        word_to_position = defaultdict()
        for idx in range(len(text) - word_length + 1):
            current_word = text[idx: idx+word_length]
            if current_word not in word_to_position:
                word_to_position.setdefault(current_word, []).append((idx, idx+word_length-1))
            else:
                word_to_position[current_word].append((idx, idx+word_length-1))
        positions = word_to_position.get(pattern)
        if pattern not in pattern_to_position:
            pattern_to_position.setdefault(pattern, []).append(positions)
        else:
            pattern_to_position[pattern].extend(positions)
        word_to_position.clear()
    return pattern_to_position


def all_occurrences_optimized(text: str, patterns: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    pattern_to_position = defaultdict()
    pattern_to_frequency = dict()
    for pattern in patterns:
        if pattern not in pattern_to_frequency:
            pattern_to_frequency[pattern] = 0
        pattern_to_frequency[pattern] += 1
    pattern_length = len(patterns[0])
    pattern_count = len(patterns)
    for i in range((len(text) - pattern_count * pattern_length) + 1):
        for j in range(0, pattern_count):
            next_word_index = i + j * pattern_length
            next_word = text[next_word_index:next_word_index + pattern_length]

            # Do not process the word we are not interested in
            if next_word not in pattern_to_frequency:
                break

            if next_word not in pattern_to_position:
                pattern_to_position.setdefault(next_word, set()).add((next_word_index, next_word_index + pattern_length-1))
            else:
                pattern_to_position[next_word].add((next_word_index, next_word_index + pattern_length-1))
    return pattern_to_position


if __name__ == '__main__':
    # start_time = time.time()
    # print(all_occurrences('catfoxcatacbdcatfox', ['cat', 'fox']))
    # end_time = time.time()
    # print(f'Total time: {(end_time - start_time)}')
    start_time = time.time()
    print(all_occurrences_optimized('catfoxcatacbdcatfox', ['cat', 'fox']))
    end_time = time.time()
    print(f'Total time: {(end_time - start_time)}')
