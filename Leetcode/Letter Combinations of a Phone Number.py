class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        self.phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        combinations = []
        self.find_combs(digits,0,[],combinations)
        return combinations

    def find_combs(self,digits,index,string,combinations):
        if index >= len(digits):
            combinations.append(''.join(str(c) for c in string))
        else:
            if digits[index] == '1' or digits[index] =='0':
                self.find_combs(digits,index+1,string,combinations)
            else:
                current_digit = digits[index]
                for i in range(len(self.phone[current_digit])):
                    string.append(self.phone[current_digit][i])
                    self.find_combs(digits,index+1,string,combinations)
                    string.pop()
