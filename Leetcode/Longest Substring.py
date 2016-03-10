class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
            
        i = longest = 0
        found = {}
        for j in range(len(s)):
            if s[j] in found and found[s[j]] == True:
                found[s[j]] = False
                while found[s[i]]:
                    found[s[i]] = False
                    i += 1
                i += 1
            
            found[s[j]] = True
            longest = max(longest,j-i+1)
        
        return longest
        