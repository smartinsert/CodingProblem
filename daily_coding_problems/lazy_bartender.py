"""
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set.
For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize.
Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy
all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
"""

from typing import Dict


def fewest_drinks_to_learn(drinks, remaining_drinks, remaining_customers, customer_by_drink):
    min_drinks = drinks

    if not remaining_customers:
        return drinks - remaining_drinks

    for drink in remaining_drinks:
        required_drinks = fewest_drinks_to_learn(drinks,
                                                 remaining_drinks - {drink},
                                                 remaining_customers - customer_by_drink[drink],
                                                 customer_by_drink)

        if len(required_drinks) < len(min_drinks):
            min_drinks = required_drinks

    return min_drinks


def get_min_drinks(preferences: Dict) -> int:
    customer_by_drink = dict()
    for customer in preferences.keys():
        for drink in preferences[customer]:
            if drink not in customer_by_drink:
                customer_by_drink[drink] = set()
            customer_by_drink[drink].add(customer)

    remaining_drinks = set(customer_by_drink.keys())
    remaining_customers = set(preferences.keys())
    return fewest_drinks_to_learn(set(customer_by_drink.keys()), remaining_drinks,
                                  remaining_customers, customer_by_drink)


if __name__ == '__main__':
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }
    print(get_min_drinks(preferences))
