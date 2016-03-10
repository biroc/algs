class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
  
        found = {}
        tail = head = max_length = 0
        while head < len(s):
            found[s[head]] = head
            head += 1
            if len(found) > 2:
                left_most = len(s)
                for key in found:
                    if found[key] < left_most:
                        left_most = found[key]
                found.pop(s[left_most], None)
                tail = left_most + 1
            max_length = max(max_length, head - tail)
        
        return max_length

        