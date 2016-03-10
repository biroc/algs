"""
Given a collection of numbers that might contain duplicates, return all possible unique
permutations.
"""

# Solution 1
def permute(input):
    elem_map = {}
    for elem in input:
        if elem in elem_map:
            elem_map[elem] += 1
        else:
            elem_map[elem] = 1

    keys = sorted(elem_map)
    elems = []
    count = []
    for key in keys:
        elems.append(key)
        count.append(elem_map[key])

    result = [0 for x in range(len(input))]
    perm_helper(elems,count,result,0)


def perm_helper(elems, count, result, level):
    if level == len(result):
        print(result)
        return

    for i in range(len(elems)):
        if count[i] == 0:
            continue

        result[level] = elems[i]
        count[i] -= 1
        perm_helper(elems,count,result,level+1)
        count[i] += 1

# Solution 2
def perm_iterative(input):
    perms = [[]]
    for n in input:
        new = []
        for list in perms:
            for i in range(len(list)+1):
                new.append(list[:i] + [n] + list[i:])
                if i < len(list) and list[i] == n: break

        perms = new
    return perms


def perm3(string,perm=""):
    if not string:
        print(perm)

    for i in range(len(string)):
        x = string[i]
        xs = string[:i] + string[i+1:]
        perm3(xs,perm + x)
