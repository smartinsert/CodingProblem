from collections import defaultdict


def max_meetings(arrival: list, departure: list):
    ordered_pairs = list(zip(arrival, departure))
    investors_met = set()
    day_to_investors = defaultdict(set)
    for investor, pair_of_days in enumerate(ordered_pairs):
        day_to_investors[pair_of_days[0]].add(investor)
        day_to_investors[pair_of_days[1]].add(investor)
    for day in day_to_investors.keys():
        if not investors_met:
            investors_met.add(day_to_investors.get(day).pop())
        else:
            while day_to_investors.get(day):
                investor_to_meet = day_to_investors.get(day).pop()
                if investor_to_meet not in investors_met:
                    investors_met.add(investor_to_meet)
                    break
    return len(investors_met)


if __name__ == '__main__':
    assert max_meetings([1, 2, 3, 3, 3], [2, 2, 3, 4, 4]) == 4
    assert max_meetings([1, 2, 3, 3, 3], [2, 2, 3, 3, 3]) == 3
    assert max_meetings([3, 1, 10, 11], [3, 11, 10, 11]) == 4