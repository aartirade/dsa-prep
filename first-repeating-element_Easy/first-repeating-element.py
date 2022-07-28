class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        d={}
        l=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in range(len(arr)):
            if d[arr[i]]>1:
                l.append(i+1)
                return l[0]
                # return arr[i]
        return -1