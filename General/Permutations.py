def perm1(string,perm=""):
    if len(string) == 0:
        print(perm)

    for i in range(len(string)):
        current = string[i]
        remaining = string[:i] + string[i+1:]
        perm1(remaining,perm+current)


def perm2(input):
    # expects a list
    if len(input) == 0:
        return input
    elif len(input) == 1:
        return [input]
    else:
        l = []
        for i in range(len(input)):
            current = input[i]
            remaining = input[:i] + input[i+1:]
            for p in perm2(remaining):
                l.append([current] + p)
    return l


def perm3(input):
    # iterative solution
    permutations = [[]]
    for n in input:
        new_perms = []
        for perm in permutations:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i]+[n]+perm[i:])
                if i < len(perm) and perm[i] == n: break
        permutations = new_perms
    return permutations