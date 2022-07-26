def reverse(S):
    stack=[]
    for i in S:
        stack.append(i)
    rev=""
    for i in range(len(stack)):
        rev=rev+stack.pop()
    return rev
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends