def answer(x):
    if not x:
        return 0
    strings = {}
    count = 0
    for s in x:
        if s in strings or s[::-1] in strings:
            continue
        else:
            strings[s] = True
            strings[s[::-1]] = True
            count += 1

    return count