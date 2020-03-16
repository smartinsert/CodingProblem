def generate_valid_ips(string, curr, all_ips):
    if len(curr) > 4 or (len(curr) < 4 and not string):
        return
    elif len(curr) == 4 and not string:
        all_ips.add(".".join(curr))
        return

    def recurse(index):
        generate_valid_ips(string[index:], curr + [string[:index]], all_ips)

    recurse(1)
    first = int(string[0])
    if first and len(string) > 1:
        recurse(2)
        if len(string) > 2 and first < 3:
            recurse(3)


def generate_valid_ip_helper(string):
    all_ips = set()
    generate_valid_ips(string, list(), all_ips)
    return all_ips


if __name__ == '__main__':
    print(generate_valid_ip_helper('2542540123'))