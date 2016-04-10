def answer(meetings):
    if not meetings:
        return 0
    _meetings = sorted(meetings,key=lambda x:x[1])
    merged_meetings = _meetings[0]
    max_meetings = 1
    for meeting_start, meeting_end in _meetings[1:]:
        if meeting_start >= merged_meetings[1]:
            max_meetings += 1
            merged_meetings[1] = meeting_end

    return max_meetings