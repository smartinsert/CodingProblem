"""
You have n ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay
for one click on this ad. You have set up n slots on your page and estimated the expected number of clicks per day for
each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.
"""


def maximum_revenue(profit_per_click, number_of_clicks_per_day):
    result = 0
    if len(profit_per_click) == 0 or len(number_of_clicks_per_day) == 0:
        return result
    for i in range(len(profit_per_click)):
        max_profit_per_click_index = max_index(profit_per_click)
        max_number_of_clicks_per_day_index = max_index(number_of_clicks_per_day)
        result += profit_per_click[max_profit_per_click_index] * number_of_clicks_per_day[max_number_of_clicks_per_day_index]
        del profit_per_click[max_profit_per_click_index]
        del number_of_clicks_per_day[max_number_of_clicks_per_day_index]
    return result


def max_index(sequence):
    maximum_idx = 0
    maximum_value = 0

    for i in range(len(sequence)):
        if sequence[i] > maximum_value:
            maximum_value = sequence[i]
            maximum_idx = i
    return maximum_idx


if __name__ == '__main__':
    print(maximum_revenue([23], [39]))
