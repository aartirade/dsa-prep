class Solution:
    def search(self, A, N):
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in range(len(A)):
            if d[A[i]]==1:
                return A[i]
        return 0