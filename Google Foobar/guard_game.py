def answer(x):
    """
    Compute digital root of non-negative integer using congruence formula.
    https://en.wikipedia.org/wiki/Digital_root
    """
    answer = x % 9
    if answer == 0 and x > 0: answer = 9
    return answer