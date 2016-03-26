class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0

        sols = [0] * (len(s) + 1)
        sols[0] = 1
        sols[1] = 1 if s[0] != '0' else 0
        for i in range(2,len(s)+1):
            last = s[i-1:i]
            if last >= '1' and last <= '9':
                sols[i] += sols[i-1]
            last_two = s[i-2:i]
            if last_two >= '10' and last_two <= '26':
                sols[i] += sols[i-2]

        return sols[-1]

