from math import factorial

mem = {}


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def answer(x, y, n):
    count = 0
    for tallest in range(x-1,n-y+1):
        left_rabbits = tallest
        right_rabbits = n - tallest - 1

        left_arrangements = arange(x-1, left_rabbits)
        right_arrangements = arange(y-1, right_rabbits)

        combs = combinations(n-1, left_rabbits)

        count += left_arrangements * right_arrangements * combs
    return str(count)


def arange(visible, total):
    if visible in mem:
        res = mem[visible]
        if total in res:
            return res[total]

    if visible > total:
        return 0
    elif visible == total:
        return 1

    count = 0
    for i in range(total):
        seen = i
        unseen = total - seen - 1
        combs = combinations(total-1, seen)
        unseen_arrangements = factorial(unseen)
        seen_arrangements = arange(visible-1,seen)
        count += combs * unseen_arrangements * seen_arrangements

    if visible not in mem:
        mem[visible] = {}

    mem[visible][total] = count
    return count