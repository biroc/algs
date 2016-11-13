def max_subsequence(matrix):
    size = 2
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            size = max(size, sol_finder(matrix,i,j))

    return size