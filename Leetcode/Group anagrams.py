class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for item in sorted(strs):
            sorted_item = ''.join(sorted(item))
            map[sorted_item] = map.get(sorted_item,[]) + [item]

        return map.values()