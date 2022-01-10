"""
Releasing software can be tricky and sometimes we release new versions of our software with bugs.
When we release a version with a bug it’s referred to as a bad release. Your product manager has just informed you that
 a bug you created was released in one of the past versions and has caused all versions that have been released since
 to also be bad. Given that your past releases are numbered from zero to N and you have a helper function
 isBadRelease(int releaseNumber) that takes a version number and returns a boolean as to whether or not the given
 release number is bad, return the release number that your bug was initially shipped in.
Note: You should minimize your number of calls made to isBadRelease().

Ex: Given the following value N…

N = 5 and release number four is the release your bug was shipped in...
isBadRelease(3) // returns false.
isBadRelease(5) // returns true.
isBadRelease(4) // returns true.


return 4.
"""
from _random import Random

def get_buggy_release_number(N: int) -> int:
    if N < 2:
        return N


def is_bad_release(release_number) -> int:
    return Random.randrange()