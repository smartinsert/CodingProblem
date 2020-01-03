"""
We define a primitive root of prime number p to be some integer g in [1, p-1] satisfying the property that all values of
g^x mod p are different where  x in [0, p-2] are different.
"""

from math import sqrt


# Returns True if n is prime
def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


""" Iterative Function to calculate (x^n)%p 
    in O(logy) */"""


def power(x, y, p):
    res = 1  # Initialize result

    x = x % p  # Update x if it is more
    # than or equal to p

    while y > 0:

        # If y is odd, multiply x with result
        if y & 1:
            res = (res * x) % p

            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


# Utility function to store prime
# factors of a number
def findPrimefactors(s, n):
    # Print the number of 2s that divide n
    primitive_roots = 1

    while n % 2 == 0:
        primitive_roots = primitive_roots << 1
        s.add(2)
        n = n // 2

    primitive_roots = primitive_roots >> 1
    # n must be odd at this po. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)) + 1, 2):

        # While i divides n, print i and divide n
        while n % i == 0:
            s.add(i)
            if i == 3:
                primitive_roots *= 3
            else:
                primitive_roots *= (i - 1)
            n = n // i


    # This condition is to handle the case
    # when n is a prime number greater than 2
    if n > 2:
        primitive_roots *= n-1
        s.add(n)
    return primitive_roots


# root of n
def findPrimitive(n):
    s = set()
    # Check if n is prime or not
    if not isPrime(n):
        return -1

    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    primitive_roots = findPrimefactors(s, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):
        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if power(r, phi // it, n) == 1:
                flag = True
                break
        if not flag:
            return '{} {}'.format(r, primitive_roots)
    return '{} {}'.format(-1, 0)


n = 37
print("Smallest primitive root of", n, "is", findPrimitive(n))
