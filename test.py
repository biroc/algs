# import unittest
#
# def max_heapify(array,i,heapsize):
#     left = 2 * i + 1
#     right = left + 1
#     largest = i
#
#     if left < heapsize and array[left] > array[largest]:
#         largest = left
#
#     if right < heapsize and array[right] > array[largest]:
#         largest = right
#
#     if largest != i:
#         array[largest], array[i] = array[i], array[largest]
#         max_heapify(array, largest, heapsize)
#
# def build_heap(array,heapsize):
#     mid = (heapsize - 1) // 2
#     for i in range(mid,-1,-1):
#         max_heapify(array,i,heapsize)
#
#
# def heapsort(array):
#     heapsize = len(array) - 1
#     build_heap(array, heapsize)
#     for i in range(len(array) - 1, 0, -1):
#         array[0], array[i] = array[i], array[0]
#         heapsize -= 1
#         max_heapify(array, 0, heapsize)
#
#
# class TestStuff(unittest.TestCase):
#
#     def test_heapify(self):
#         array = [10,7,8,9,6,5,4,3,2,1]
#         max_heapify(array, 1, len(array))
#         self.assertEqual(array, [10,9,8,7,6,5,4,3,2,1])
#
#     def test_heapsort(self):
#         array = [10,7,8,9,6,5,4,3,2,1]
#         heapsort(array)
#         self.assertEqual(array, [1,2,3,4,5,6,7,8,9,10])

def one_away(first,second):
    if abs(len(first) - len(second)) > 1:
        return False
    m = len(first)
    n = len(second)
    if m > n:
        return one_away(second, first)
    diff = n - m
    i = 0
    while i < m and first[i] == second[i]:
        i += 1
    if i == m:
        return diff == 1
    if diff == 0:
        i += 1
    while i < m and first[i] == second[i + diff]:
        i += 1
    return i == m


def rotate_90(matrix):
    length = len(matrix) - 1
    layers = len(matrix) // 2
    for curr_layer in range(layers):
        for i in range(curr_layer, length - curr_layer):
            top = matrix[curr_layer][i]
            # left - > top
            matrix[curr_layer][i] = matrix[length - i][curr_layer]
            # bottom -> left
            matrix[length - i][curr_layer] = matrix[length - curr_layer][length - i]
            # right -> bottom
            matrix[length - curr_layer][length - i] = matrix[i][length - curr_layer]
            # top - > right
            matrix[i][length - curr_layer] = top

    return matrix

def firstRepeatingLetter(s):
    dict = {}
    lowest_index = len(s)
    lowest_letter = ''
    for index, c in enumerate(s) :
        if c in dict:
            if dict[c] < lowest_index:
                lowest_letter = c
                lowest_index = dict[c]
        else:
            dict[c] = index

    return lowest_letter
