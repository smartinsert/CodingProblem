"""
You are serving people in a lunch line and need to ensure each person gets a “balanced” meal.
A balanced meal is a meal where there exists the same number of food items as drink items.
Someone is helping you prepare the meals and hands you food items (i.e. F) or a drink items (D) in the order
specified by the items string. Return the maximum number of balanced meals you are able to create without being able
to modify items. Note: items will only contain F and D characters.

items = "FDFDFD", return 3
the first "FD" creates the first balanced meal.
the second "FD" creates the second balanced meal.
the third "FD" creates the third balanced meal.

items = "FDFFDFDD", return 2
"FD" creates the first balanced meal.
"FFDFDD" creates the second balanced meal.
"""


def number_of_meals(items: str) -> int:
    if len(items) < 2:
        return 0
    num_f, num_d, balanced_meals = 0, 0, 0
    for meal in items:
        if meal == 'F':
            num_f += 1
        elif meal == 'D':
            num_d += 1
        if num_f == num_d:
            balanced_meals += 1
            num_f, num_d = 0, 0
    return balanced_meals


print(number_of_meals('FDFDFD'))
print(number_of_meals('FDFFDFDD'))



