"""
Recursion and Dynamic Programming
"""

"""
8.1 Triple Step
"""


def triple_step(N, memo):
    if N < 0:
        return 0
    if N == 0:
        return 1
    if memo[N] == 0:
        memo[N] = triple_step(N-1,memo) + triple_step(N-2,memo) + triple_step(N-3,memo)

    return memo[N]

"""
8.2 Robot in a grid
"""
class Solution:
    def __init__(self):
        self.paths = []  # list of tuples: (row,col)

    def create_paths(self, matrix,row,col,n,m):
        if row == n-1 and col == m-1:
            print(' '.join(str(cell) for cell in self.paths))

        if row >= n or col >= m:
            return

        if matrix[row][col] == 1:
            return

        self.paths.append((row,col))
        self.create_paths(matrix,row+1,col,n,m)
        self.paths.pop()

        self.paths.append((row,col))
        self.create_paths(matrix,row,col+1,n,m)
        self.paths.pop()

"""
8.4 Power Set
"""

def subsets(start,set,current,output):
    for i in range(start,len(set)):
        current.append(set[i])
        output.append(' '.join(str(j) for j in current))
        if i < len(set) - 1:
            subsets(i+1,set,current,output)
        current.pop()

    return output



"""
8.5 Recrusive Multiply
"""
def multiply_recursive(a,b):
    if not b:
        return 0

    a = a + multiply_recursive(a, b-1)
    return a


"""
8.9 Parens
"""


def compute(n):
    string_array = ['.'] * (2*n)
    list = []
    compute_parens(list,n,n,string_array,0)
    return list

def compute_parens(list,left,right,current,count):
    if right < 0 or left > right:
        return

    if left == 0 and right == 0:
        list.append(current)
    else:
        if left > 0:
            current[count] = '('
            compute_parens(list,left-1,right,current,count+1)

        if right > left:
            current[count] = ')'
            compute_parens(list,left,right-1,current,count+1)