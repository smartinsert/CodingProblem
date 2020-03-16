"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0
prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""


def all_possible_address(string):
    valid_addresses = set()
    current_address = list()
    all_possible_address_rec(string, current_address, valid_addresses)
    return valid_addresses


def all_possible_address_rec(string, current_path, valid_addresses):
    if len(current_path) > 4 or (len(current_path) < 4 and not string):
        return
    if len(current_path) == 4 and not string:
        valid_addresses.add('.'.join(current_path))
        return

    def recurse(index):
        all_possible_address_rec(string[index:], current_path + [string[:index]], valid_addresses)

    # recurse with one digit at a time
    recurse(1)
    # Get the first digit after recursing with 1 digit at a time
    first = int(string[0])
    if first and len(string) > 1:
        # recurse with 2 characters at a time
        recurse(2)
        # recurse with 3 digits at a time only when the first digit and the remaining string
        # has a length greater than 2
        if first < 3 and len(string) > 2:
            recurse(3)


if __name__ == '__main__':
    print(all_possible_address('25525511135'))

