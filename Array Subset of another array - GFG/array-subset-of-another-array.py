#User function Template for python3

def isSubset( a1, a2, n, m):
    set1=set(a1)
    set2=set(a2)
    
    i=set2.intersection(set1)
    if i==set2:
        return "Yes"
    else:
        return "No"
    # count=0
    # for i in range(0, n):
    #     for j in range(0, m):
    #         if a1[i] == a2[j]:
    #             count+=1

    # if count==m:
    #     return "Yes"
    # else:
    #     return "No"
    
    
    # i = 0
    # j = 0
    # for i in range(n):
    #     for j in range(m):
    #         if(a1[i] == a2[j]):
    #             break
    #     if (j == m):
    #         return "No"
     
    # return "Yes"
  


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends