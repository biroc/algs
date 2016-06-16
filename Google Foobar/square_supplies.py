import math
def is_square(n):
    # Function to check if a number is a perfect square.
    # math.sqrt always returns float.
    sqrt_n = int(math.sqrt(n))
    return sqrt_n**2 == n


def answer(n):
    """
    Basically this problem is one where we need to find the minimum
    number of perfect squares or number 'n' can be summed up to.

    Lagrange’s four-square theorem tells us that any natural number
    can be represented as a sum of four integer squares. So the maximum
    number of perfect squares is 4.

    Cases:
    - The number itself is a perfect square -> return 1
    - The number can be written in the form 4^k(8m+7) -> return 4
    - The number can be broken down into two perfect squares -> return 2
    - Otherwise return 3
    """
    # check for perfect square
    if is_square(n):
        return 1

    # check for form '4^k(8m+7)'
    while (n % 4) == 0:
        n >>= 2

    if (n % 8) == 7:
        return 4

    # check if the number can be broken down into 2 perfect squares
    sqrt_n = int(math.sqrt(n))
    for i in range(1,sqrt_n+1):
        if is_square(n - i * i):
            return 2

    return 3


