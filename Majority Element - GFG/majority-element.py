#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        h=N//2
        d={}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        keymax=max(zip(d.values(),d.keys()))[0]
        keyval=max(zip(d.values(), d.keys()))[1]
        
        if keymax>h:
            return keyval
        return -1
                
        
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends