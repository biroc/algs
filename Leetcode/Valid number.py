class Solution(object):
    def isNumber(self, s):
        if not s:
            return False
        i = 0
        n = len(s)
        isValid = False
        while i < n and s[i].isspace():
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
        while i < n and s[i].isdigit():
            isValid = True
            i += 1
        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                isValid = True
        if isValid and i < n and s[i] == 'e':
            i += 1
            isValid = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                    i += 1
            while i < n and s[i].isdigit():
                isValid = True
                i += 1

        while i < n and s[i].isspace():
            i += 1
        return isValid and i == n