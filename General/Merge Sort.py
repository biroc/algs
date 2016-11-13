def quicksort(array,low,high):
    if low < high:
        p = partition(array,low,high)
        quicksort(array,low,p-1)
        quicksort(array,p+1,high)


def partition(array,low,high):
    pivot_index = (low+high) // 2
    pivot = array[pivot_index]
    array[pivot_index], array[high] = array[high], array[pivot_index]
    swapIndex = low
    for i in range(low,high):
        if array[i] < pivot:
            array[i], array[swapIndex] = array[swapIndex], array[i]
            swapIndex += 1
    array[swapIndex], array[high] = array[high], array[swapIndex]

    return swapIndex


def merge(array, left,right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        array[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        array[k] = right[j]
        k += 1
        j += 1
    return array

