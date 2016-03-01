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

def one_away(first,second):
    diff = abs(len(first) - len(second))
    if diff > 1:
        return False

    changes = 0
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] != second[j]:
            if not diff:
                i += 1
                j += 1
                changes += 1
            else:
                if first[i+1] == second[j]:
                    i += 2
                    j += 1
                elif first[i] == second[j+1]:
                    i += 1
                    j += 2
                else:
                    return False
        else:
            i += 1
            j += 1
    return changes < 2

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

"""
1.8 Zero Matrix
"""


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