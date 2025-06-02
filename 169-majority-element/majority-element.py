class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[n//2]==nums[0] or nums[n//2]==nums[-1] or  nums[n//2]==nums[n//2-1]:
            return nums[n//2]
