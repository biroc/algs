class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return None
        start = end = 0
        for i in range(len(s)):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i,i+1)
            len_max = max(len1,len2)
            if len_max > end - start:
                start = i - (len_max-1) // 2
                end = i + len_max // 2

        return s[start:end+1]

    def expand(self,string,left,right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return right - left - 1
