class Solution(object):
    def wordPatternMatch(self, pattern, str):
        map, substring_set = {}, set()
        return self.is_match(str,pattern,0,0,map,substring_set)

    def is_match(self,string,pattern,istr,ip,map,substring_set):
        if istr == len(string) and ip == len(pattern): return True
        if istr == len(string) or ip == len(pattern): return False

        pattern_character = pattern[ip]
        if pattern_character in map:
            substring = map[pattern_character]

            if not string.startswith(substring,istr):
                return False

            return self.is_match(string,pattern,istr + len(substring),ip+1,map,substring_set)

        for end in range(istr,len(string)):
            substring = string[istr:end+1]

            if substring in substring_set:
                continue

            map[pattern_character] = substring
            substring_set.add(substring)

            if self.is_match(string,pattern,end+1,ip+1,map,substring_set):
                return True

            map.pop(pattern_character, None)
            substring_set.remove(substring)

        return False