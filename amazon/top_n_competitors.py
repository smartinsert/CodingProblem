import re
from heapq import *


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    if not competitors or not reviews:
        return []
    if topNCompetitors == 0:
        return []

    competitor_frequency_quote = dict()

    competitor_to_count = dict()

    # (x, y) where x is frequency count and y is the quote number
    for competitor in competitors:
        if competitor not in competitor_frequency_quote:
            competitor_frequency_quote[competitor] = (0, 0)

    # For each review count the number of occurrences of competitors in every quote
    for review in reviews:
        # Check if competitor has not been counted more than once in a review
        updated_competitor_count = {review: False for review in reviews}
        unique_reviews = set(review.lower().split())
        if name in unique_reviews:
            word = re.sub('[^a-z]', '', name)
            if word not in competitor_to_count:
                competitor_to_count[word] = 0
            competitor_to_count[word] += 1
        # for word in unique_words:
        #     word = re.sub('[^a-z]', '', word)
        #     if word in competitor_frequency_quote:
        #         current_frequency, current_quote = competitor_frequency_quote.get(word)[0], \
        #                                            competitor_frequency_quote.get(word)[1]
        #         if not updated_competitor_count.get(word):
        #             current_quote += 1
        #             updated_competitor_count[word] = True
        #
        #         competitor_frequency_quote[word] = (current_frequency + 1, current_quote)

    # Remove irrelevant competitors
    # for competitor in competitors:
    #     if competitor_frequency_quote.get(competitor)[0] == 0:
    #         del competitor_frequency_quote[competitor]

    sorted_competitors = {k: v for k,v in sorted(competitor_to_count.items(), key= lambda item: item[1])}
    top_competitor = []
    i = 0
    for key in sorted_competitors.keys():
        if i < topNCompetitors:
            top_competitor.append((key, sorted_competitors.get(key)))
        i += 1

    print(top_competitor)
    # Now we have the map of all relevant competitors

    # If the topNCompetitors > numCompetitors: we return the relevant competitor names
    if topNCompetitors > numCompetitors:
        return [competitor for competitor in competitor_frequency_quote.keys()]

    # Now we create a max heap with (-freq, -count, competitor) as python's heap creates a min heap
    # It is ordered by frequency, count and competitor name
    top_competitor_heap = []

    for competitor in competitor_frequency_quote.keys():
        frequency_and_appearances = competitor_frequency_quote.get(competitor)
        total_frequency = frequency_and_appearances[0]
        total_appearances = frequency_and_appearances[1]
        top_competitor_heap.append((-1 * total_frequency, -1 * total_appearances, competitor))

    heapify(top_competitor_heap)

    # Get top N competitors
    top_competitors = []
    for competitor in range(topNCompetitors):
        top_competitors.append(heappop(top_competitor_heap)[2])
        if not top_competitor_heap:
            break
    return top_competitors


if __name__ == '__main__':
    topNCompetitors(6, 2, ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular'], 1,
                    ["newshop is providing good services in the city; everyone should use newshop"])