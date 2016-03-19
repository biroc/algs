def subarray_sum(array):
    dict = {}
    sum = 0
    dict[0] = 0
    for i in range(len(array)):
        sum += array[i]
        if sum in dict:
            return [dict[sum], i]

        dict[sum] = i

    return [-1,-1]