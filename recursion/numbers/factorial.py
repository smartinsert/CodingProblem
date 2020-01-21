

def factorial(target_number):
    # Base case
    if target_number == 1:
        return 1
    # Recursive Case
    else:
        return target_number * factorial(target_number - 1)
    

if __name__ == '__main__':
    target_number = 5
    print(factorial(5))