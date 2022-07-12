class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        # dict={}
        # for i in range(len(nums)):
        #     if target-nums[i] in dict:
        #         prev=dict[target-nums[i]]
        #         return[prev,i]
        #     dict[nums[i]]=i

        
        
        
        
        
        
        
        
        
        
        
        