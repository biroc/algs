class Solution(object):
    def wordPattern(self, pattern, str):
        strings = str.split(' ')
        if len(strings) != len(pattern): return False
        strings_map, patterns_map = {}, {}
        for i in range(len(strings)):
            if strings[i] not in strings_map: strings_map[strings[i]] = 0
            if pattern[i] not in patterns_map: patterns_map[pattern[i]] = 0
            strings_map[strings[i]] += 1
            patterns_map[pattern[i]] += 1
            if strings_map[strings[i]] != patterns_map[pattern[i]]: return False

        return True
