def select(array,low,high,n):
    if low == high:
        return array[low]

    pivot_index = (low+high) // 2
    pivot_index = partition(array,low,high,pivot_index)
    if pivot_index == n:
        return array[n]
    elif pivot_index < n:
        return select(array,pivot_index+1,high,n)
    else:
        return select(array,low,pivot_index-1,n)


def partition(array,low,high,pivot_index):
    pivot = array[pivot_index]
    array[high], array[pivot_index] = array[pivot_index], array[high]
    startIndex = low
    for i in range(low,high):
        if array[i] < pivot:
            array[i], array[startIndex] = array[startIndex], array[i]
            startIndex += 1
    array[high], array[startIndex] = array[startIndex], array[high]

    return startIndex