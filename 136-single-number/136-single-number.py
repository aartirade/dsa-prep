class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in range(len(nums)):
            if d[nums[i]]==1:
                return nums[i]
        
        