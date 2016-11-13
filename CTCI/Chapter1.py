"""
1.1 Is Unique
"""

def is_unique(string):
    if not string:
        return True
    hash = {}
    for c in string:
        if c in hash:
            return False
        else: hash[c] = True

    return True


def is_unique2(string):
    if not string:
        return True
    sort_s = sorted(string)
    for i in range(1, len(string)):
        if sort_s[i-1] == sort_s[i]:
            return False

    return True

"""
1.2 Check Permutation
"""


def is_permutation(first,second):
    if len(first) != len(second):
        return False

    hash = {}
    for c in first:
        if c in hash:
            hash[c] += 1
        else: hash[c] = 1

    for s in second:
        if not s in hash:
            return False
        hash[s] -= 1
        if hash[s] < 0:
            return False

    return True

"""
1.3 URLify
INPUT: "Mr John Smith"
OUTPUT: "Mr%20John%20Smith"
"""


def urlify(string):
    spaces = 0
    for c in string:
        if c == ' ':
            spaces += 1

    new_length = len(string) + 2*spaces
    urlified = ['.'] * new_length
    i = len(string)-1
    j = new_length - 1
    while i >= 0:
        if string[i] == ' ':
            urlified[j] = '0'
            urlified[j-1] = '2'
            urlified[j-2] = '%'
            j -= 3
        else:
            urlified[j] = string[i]
            j -= 1
        i -= 1

    return ''.join(urlified)

"""
1.4 Palindrome permutation
"""
def is_pal_permut(string):
    hash = {}
    for c in string:
        if c in hash:
            hash[c] += 1
        elif c != ' ':
            hash[c] = 1

    uneven = 0
    for key in hash:
        if hash[key] % 2 != 0:
            uneven += 1
            if uneven > 1:
                return False

    return True

"""
1.5 One Away
"""


def isOneEditDistance(self, s, t):
    """
	:type s: str
	:type t: str
	:rtype: bool
	"""
    m = len(s)
    n = len(t)

    diff = abs(m - n)

    if diff > 1:
        return False

    if m < n:
        return self.isOneEditDistance(t, s)

    i = 0
    while i < n and s[i] == t[i]:
        i += 1

    if diff == 0:
        i += 1

    while i < n and s[i + diff] == t[i]:
        i += 1

    return i == n

"""
1.6 String Compression
"""
def string_compression(string):
    if not string:
        return None
    current = string[0]
    counter = 1
    new_string = ""
    for i in range(1,len(string)):
        if string[i] != current:
            new_string += current + str(counter)
            counter = 1
            current = string[i]
        else:
            counter += 1

    if counter > 0:
        new_string += current + str(counter)

    return new_string if len(new_string) < len(string) else string


"""
1.7 Rotate Matrix
"""


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
"""
1.8 Zero Matrix
"""


def zero_matrix(matrix):
    zeroRow = False
    zeroCol = False

    # Check if first row has a zero
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            zeroRow = True
            break

    # Check if first col has a zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            zeroCol = True
            break

    # Check for zeros in all spaces beside first row/col
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][j] = 0

    # Nullify rows and cols
    for i in range(1,len(matrix[0])):
        if matrix[0][i] == 0:
            nullifyCol(i,matrix)

    for i in range(1,len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(i,matrix)

    if zeroRow:
        nullifyRow(0,matrix)

    if zeroCol:
        nullifyCol(0,matrix)


def nullifyRow(index, matrix):
    for i in range(len(matrix[index])):
        matrix[index][i] = 0


def nullifyCol(index, matrix):
    for i in range(len(matrix)):
        matrix[i][index] = 0


"""
1.9 String Rotation
"""


def is_substring(bigger,smaller):
    if smaller in bigger:
        return True
    else:
        return False

def is_rotation(s1,s2):
    if len(s1) != len(s2) or not s1 or not s2:
        return False
    return is_substring(s1+s1,s2)