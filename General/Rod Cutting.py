class Solution(): #[0,1,5,8,9,10,17,17,20,24,30]
    def memo_cut_rod(self,p,n):
        self.solutions = [-1] * (n+1)
        return self.memo_cut_rod_aux(p,n)

    def memo_cut_rod_aux(self,p,n):
        if self.solutions[n] >= 0:
            return self.solutions[n]
        if n == 0:
            q = 0
        else:
            q = -99999
            for i in range(n):
                q = max(q, p[i] + self.memo_cut_rod_aux(p,n-i-1))

        self.solutions[n] = q
        return q

    def bottom_up_cutrod(self,p,n):
        sols = [0] * (n+1)
        for i in range(1,n+1):
            q = -9999
            for j in range(1,i+1):
                q = max(q, p[j] + sols[i-j])
            sols[i] = q

        return  sols[n]