import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n3=nums1+nums2
        n3.sort()
        n=len(n3)
        return statistics.median(n3)
        # mid=(n-1)//2
        # if n%2==0:
        #     a=n3[mid]+n3[mid-1]
        #     return a/2
        # else:
        #     return n3[mid]
        