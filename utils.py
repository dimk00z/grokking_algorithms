from random import randint
from time import monotonic
from functools import wraps


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = monotonic()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = monotonic() - start
            print()
            print(
                f"Total execution time {func.__name__}: {end_:.15f} ms"
            )

    return _time_it


def create_ordered_list(start: int = 0,
                        step: int = 1,
                        end: int = 100):
    return [number+1 for number in range(start, end, step)]


def create_random_list(max_value=100):
    return [randint(0, max_value) for random_value in range(max_value)]


def findSum(str1, str2):

    # Before proceeding further, make sure length
    # of str2 is larger.
    if len(str1) > len(str2):
        temp = str1
        str1 = str2
        str2 = temp

    # Take an empty string for storing result
    str3 = ""

    # Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)
    diff = n2 - n1

    # Initially take carry zero
    carry = 0

    # Traverse from end of both strings
    for i in range(n1-1, -1, -1):

        # Do school mathematics, compute sum of
        # current digits and carry

        sum = ((ord(str1[i])-ord('0')) +
               int((ord(str2[i+diff])-ord('0'))) + carry)

        str3 = str3+str(sum % 10)

        carry = sum//10

    # Add remaining digits of str2[]
    for i in range(n2-n1-1, -1, -1):

        sum = ((ord(str2[i])-ord('0'))+carry)
        str3 = str3+str(sum % 10)
        carry = sum//10

    # Add remaining carry
    if (carry):
        str3+str(carry+'0')

    # reverse resultant string
    str3 = str3[::-1]

    return str3


def print_2d_list(array):
    for row in array:
        print(' '.join([str(item) for item in row]))


def get_matrix(x, y):
    return [[0 for y in range(y+1)] for x in range(x+1)]
