def ExtractNumber(self,S):
        #code here
        res=[]
        s=S.split()
        for i in s:
            if '9' not in i:
                if i.isdigit():
                    res.append(int(i))
            
        if len(res)==0:
            return -1
        else: 
            return(max(res))
        
       

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends