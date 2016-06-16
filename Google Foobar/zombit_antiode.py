def answer(meetings):
    # Maximum number of non-overlapping meetings problem
    # The idea of the algorithm is to sort the meetings by end time
    # and iterate through them comparing the start time of the current
    # meeting with the end time of the previous one

    if not meetings:
        return 0

    # sort meetings by end time to optimize for those ending fastest
    meetings = sorted(meetings, key=lambda x:x[1])

    # initialize with first meetings
    current_start, current_end = meetings[0]
    num_meetings = 1

    for start, end in meetings[1:]:
        # if we have found a new non-overlapping meeting
        if start >= current_end:
            num_meetings += 1
            # update end time
            current_end = end

    return num_meetings