class Solution(object):
    def reverseWords(self, s):
        self.reverse(s,0,len(s))
        i = 0
        for j in range(len(s)+1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s,i,j)
                i = j + 1
        
    def reverse(self,s,start,end):
        for i in range((end-start)//2):
            s[start+i],s[end-i-1] = s[end-i-1], s[start+i]
        