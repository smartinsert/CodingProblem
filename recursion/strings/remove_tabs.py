

def remove(string):
    # Base Case
    if not string:
        return ''

    if string[0] == '\t' or string[0] == ' ':
        return remove(string[1:])
    else:
        string[0] + remove(string[1:])