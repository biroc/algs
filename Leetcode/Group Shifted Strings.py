class Solution(object):
    def groupStrings(self, strings):
        map = {}
        for string in strings:
            string_code = self.getCode(string)
            if string_code in map:
                list = map[string_code]
            else:
                list = []
            list.append(string)
            map[string_code] = list

        result = [sorted(a) for a in map.values()]
        return result

    def getCode(self,string):
        code_string = ""
        for i in range(1,len(string)):
            val = (ord(string[i]) - ord(string[i-1]) + 26) % 26
            code_string += str(val)
        return code_string