class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
  
        found = {}
        tail = head = max_length = 0
        # use sliding window with constraint of maximum
        # 2 distinct elements in the hashmap
        # when 3 distinct elements are found, we want to eliminate
        # the character whos last found position is the left-most,
        # to make sure we have only 2 distinct characters going forward
        # we start from that position + 1
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