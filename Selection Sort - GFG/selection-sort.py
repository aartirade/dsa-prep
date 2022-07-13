#User function Template for python3

class Solution: 
    def select(self, arr, i):
        pass
        # code here 
    
    def selectionSort(self, arr,n):
        for step in range(n):
            min_i=step
            
            for i in range(step+1,n):
                if arr[i]<arr[min_i]:
                    min_i=i
            arr[step],arr[min_i]=arr[min_i],arr[step]
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends