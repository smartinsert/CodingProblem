"""
You work on a team whose job is to understand the most sought after toys for the holiday season.
A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles.
You need to take these quotes and identify which toys are mentioned most frequently. Write an algorithm that identifies
the top N toys out of a list of quotes and list of toys.
"""
import re
from heapq import *


def top_n_buzzwords(num_toys, top_toys, toys, num_quotes, quotes):
    if not toys or not quotes:
        return []
    if top_toys == 0:
        return []
    toy_frequency_quote = dict()
    for toy in toys:
        if toy not in toy_frequency_quote:
            toy_frequency_quote[toy] = (0, 0)
    # Dict to store toy buzzword as key and value as tuple in form of (total_freq, total_quotes)
    # So we will have dict like: {'elmo': (4, 3), 'elsa': (4, 2)}
    # Here, 'elmo': (4, 3) means word 'elmo' occurs total 4 times throughout all the quotes and it comes in 3 different quotes.
    #
    # We will first create entry for all toys with (total_freq, total_quotes) = (0, 0)
    for quote in quotes:
        # We need this updated_quote_count dict so that we don't increment the quote count for a buzzword more than once,
        # in case if it occurs multiple times in a single quote
        updated_quote_count = {toy: False for toy in toys}
        # Convert all the words to lowercase and split them.
        # Go through all the words of a quote and:
        # - Remove all the extra characters from the words except "a-z". Basically we replace them with '' using regex.
        for word in quote.lower().split():
            word = re.sub('[^a-z]', '', word)
            if word in toy_frequency_quote:
                # Get current frequency and quote count
                current_frequency, current_quote = toy_frequency_quote.get(word)[0], toy_frequency_quote.get(word)[1]
                # If the current quote count is not already incremented for word w, do it and mark it in updated_quote_count
                if not updated_quote_count.get(word):
                    current_quote += 1
                    updated_quote_count[word] = True

                # Update frequency and quote values
                toy_frequency_quote[word] = (current_frequency + 1, current_quote)

    # Remove all the toys from the dict which are not their in the quotes
    for toy in toys:
        if toy_frequency_quote.get(toy)[0] == 0:
            del toy_frequency_quote[toy]

    # Now we have the map of all the buzzwords from toys which appeared in quotes
    # First thing to check is if topToys (i.e. number of top toys/buzzwords to return) is > total numToys (i.e. total buzzwords)
    #   - If it is, then as per the given requirement, we just need to return the list of present buzzwords in quotes.
    #
    # If we return here, then all the computation stops and we are done.
    if top_toys > num_toys:
        return [toy for toy in toy_frequency_quote.keys()]

    buzzword_heap = []
    # Go through all buzzwords from toy_freq_quote dict and take their (total_freq, total_quote_count).
    # Add it to the buzzword_heap as (-1*total_freq, -1*total_quote_count, buzzword)
    #
    # - Since we want to order by maximum total_freq and after that maximum total_quote_count, we will multiply them with -1 when
    #   pushing into the heap.
    # - We do that because in Python heapq.heapify(list), the heap created is min-heap.
    # - If we don't multiply those numbers by -1, then we will output with minimum total_freq and total_quotes.
    # - Also, we keep the ordering like (total_freq, total_quote_count, buzzword)
    #   because we first have to get the buzzword with max frequency, after that with max quote_count, and in the end
    #   in alphabetical order of buzzwords themselves.
    for toy in toy_frequency_quote.keys():
        frequency_and_appearances = toy_frequency_quote.get(toy)
        total_frequency = frequency_and_appearances[0]
        total_appearances = frequency_and_appearances[1]
        buzzword_heap.append((-1*total_frequency, -1*total_appearances, toy))
    heapify(buzzword_heap)

    # Final Result
    top_buzzwords = []
    for i in range(top_toys):
        top_buzzwords.append(heappop(buzzword_heap)[2])
        if not buzzword_heap:
            break
    return top_buzzwords


if __name__ == '__main__':
    num_toys, top_toys, num_quotes = 6, 2, 6
    toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
    quotes = [
        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
        "The new Elmo dolls are super high quality",
        "Expect the Elsa dolls to be very popular this year, Elsa!",
        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
        "For parents of older kids, look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"
    ]
    print(top_n_buzzwords(num_toys=num_toys, top_toys=top_toys, toys=toys, num_quotes=num_quotes, quotes=quotes))