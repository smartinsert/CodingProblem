def merge(str1, str2):
    # Base case 1
    if str1 == '':
        if str2 == '':
            return ''
        return str2
    # Base case 2
    elif str2 == '':
        return str1

    elif str1[0] > str2[0]:
        return str2[0] + merge(str1, str2[1:])
    return str1[0] + merge(str1[1:], str2)


if __name__ == '__main__':
    print(merge('stu', 'abc'))