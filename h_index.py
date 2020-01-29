"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each.

If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].

Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.
"""

from typing import List
from collections import defaultdict


def calculate_h_index(papers_with_citations: List[int]) -> int:
    papers_with_citations.sort()
    citation_to_occurences = defaultdict()
    paper_to_citations_greater_than_itself = dict()
    relevant_papers = set()
    for idx, citation in enumerate(papers_with_citations):
        if citation not in citation_to_occurences:
            citation_to_occurences[citation] = []
        citation_to_occurences[citation].append(idx)
    for key in citation_to_occurences.keys():
        if key not in paper_to_citations_greater_than_itself:
            paper_to_citations_greater_than_itself[key] = 0
        paper_to_citations_greater_than_itself[key] = len(papers_with_citations) - min(citation_to_occurences[key]) + 1
    for key in paper_to_citations_greater_than_itself:
        if paper_to_citations_greater_than_itself.get(key) >= key:
            relevant_papers.add(key)
    return max(relevant_papers)


if __name__ == '__main__':
    print(calculate_h_index([4, 3, 0, 1, 5]))
    print(calculate_h_index([5, 3, 5, 1, 5, 5, 5]))
    print(calculate_h_index([4, 1, 0, 1, 1]))
    print(calculate_h_index([4, 4, 4, 5, 4]))