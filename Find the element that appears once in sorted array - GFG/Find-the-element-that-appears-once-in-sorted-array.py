class Solution:
    def findOnce(self,arr : list, n : int):
        a=2 * sum(set(arr))- sum(arr)
        return a
        # Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends