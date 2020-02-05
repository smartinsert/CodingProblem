import re
from heapq import *


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    print("Reviews: {}".format(reviews))
    if not competitors or not reviews:
        return []
    if topNCompetitors == 0:
        return []

    competitor_frequency_reviews = dict()

    # (x, y) where x is frequency count and y is the quote number
    for competitor in competitors:
        if competitor not in competitor_frequency_reviews:
            competitor_frequency_reviews[competitor] = (0, 0)

    # For each review count the number of occurrences of competitors in every quote
    for review in reviews:
        # Check if competitor has not been counted more than once in a review
        updated_competitor_count = {competitor: False for competitor in competitors}
        for word in review.lower().split():
            word = re.sub('[^a-z]', '', word)
            if word in competitor_frequency_reviews:
                current_frequency, current_review_occurrence_count = competitor_frequency_reviews.get(word)[0], \
                                                   competitor_frequency_reviews.get(word)[1]
                if not updated_competitor_count.get(word):
                    current_review_occurrence_count += 1
                    updated_competitor_count[word] = True

                competitor_frequency_reviews[word] = (current_frequency + 1, current_review_occurrence_count)

    # Remove irrelevant competitors
    for competitor in competitors:
        if competitor_frequency_reviews.get(competitor)[0] == 0:
            del competitor_frequency_reviews[competitor]

    # Now we have the map of all relevant competitors

    # If the topNCompetitors > numCompetitors: we return the relevant competitor names
    if topNCompetitors > numCompetitors:
        return [competitor for competitor in competitor_frequency_reviews.keys()]

    # Now we create a max heap with (-freq, -count, competitor) as python's heap creates a min heap
    # It is ordered by frequency, count and competitor name
    top_competitor_heap = []

    for competitor in competitor_frequency_reviews.keys():
        frequency_and_appearances = competitor_frequency_reviews.get(competitor)
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