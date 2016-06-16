def answer(intervals):
    if not intervals:
        return 0
    # initially sort all intervals using the start date
    intervals = sorted(intervals, key=lambda x:x[0])

    total_time = 0

    running_start, running_end = intervals[0]
    for interval in intervals[1:]:
        start, end = interval
        if running_end >= start:
            running_end = max(running_end,end)
        else:
            total_time += running_end - running_start
            running_start, running_end = start, end

    total_time += running_end - running_start
    return total_time