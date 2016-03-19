import sys

def bs(array, low , high, value):
    if high - low <= 1:
        return min(abs(array[low]-value), abs(array[high] - value))

    mid = (high + low) // 2
    if value == array[mid]: return 0
    if value > array[mid]:
        return bs(array,mid+1,high,value)
    else:
        return bs(array,low,mid-1,value)


def smallest_difference(A, B):
    A = sorted(A)
    minimum = sys.maxsize
    for i in range(len(B)):
        minimum = min(minimum,bs(A,0,len(A)-1,B[i]))

    return minimum