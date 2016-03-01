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
