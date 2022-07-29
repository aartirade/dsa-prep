def findMissing(A,B,N,M):
    d={}
    l=[]
    for i in B:
        if i not in d:
            d[i]=i
    
    for i in A:
        if i not in d:
            l.append(i)
    return l
    
    
    
    #approach-2
    # l=[]
    # for i in A:
    #     if i not in B:
    #         l.append(i)
    # return l
    
    
    #approach-3
    # a=set(A)
    # b=set(B)
    # c=a.difference(b)
    # return sorted(list(c))
        
  

#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends