def is_palindrome(test_variable):
    if len(test_variable) <= 1:
        return True
    if test_variable[0] == test_variable[-1]:
        return True
    return is_palindrome(test_variable[1:-2])

if __name__ == '__main__':
    print(is_palindrome('Educ'))