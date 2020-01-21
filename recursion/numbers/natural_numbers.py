

def directly_print_natural_numbers(lower_range, upper_range):
    # Base case
    if lower_range > upper_range:
        return

    print(lower_range)

    # Recursive Case
    directly_print_natural_numbers(lower_range + 1, upper_range)


def indirectly_print_natural_numbers(lower_range, upper_range):
    if lower_range <= upper_range:
        print(lower_range)
        lower_range += 1
        helper_function(lower_range, upper_range)
    else:
        return


def helper_function(lower_range, upper_range):
    if lower_range <= upper_range:
        print(lower_range)
        lower_range += 1
        indirectly_print_natural_numbers(lower_range, upper_range)
    else:
        return


if __name__ == '__main__':
    n = 5
    indirectly_print_natural_numbers(1, n)