class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in range(len(nums)):
            if d[nums[i]]>=2:
                return nums[i]
        
                
        