def partition(array, k):
    if not array:
        return 0

    s = 0
    b = len(array) - 1
    while s < b:
        if array[s] < k:
            s += 1
            continue
        if array[b] >= k:
            b -= 1
            continue
        array[s], array[b] = array[b], array[s]

    for i in range(len(array)):
        if array[i] >= k:
            return i

    return len(array)