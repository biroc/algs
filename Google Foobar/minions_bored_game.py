def answer(t,n):
    """
    DP approach to check possible moves at each positon
    by computing current, before and after position possible moves.
    """
    current = [0] * n
    current[n-1] = 1
    last = [0] * n
    for i in range(t):
        current, last = last, current
        for j in range(n):

            # If we 'stay' on this current position.
            current[j] = last[j]

            # From last position we can only stay.
            if (j+1) == n:
                continue

            # If we aren't on the first position
            # add moves from left position
            if j != 0:
                current[j] += last[j-1]

            current[j] += last[j+1]

    return current[0] % 123454321