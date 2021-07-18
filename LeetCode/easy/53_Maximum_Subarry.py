# O(n^2) Time Limit Exceed
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n):
            for j in range(i,n):
                res=max(res,sum(nums[i:j+1]))
        return res

# Answer(Kadane's Algorithm)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n):
            if i>0:
                nums[i] = max(nums[i-1]+nums[i],nums[i])
            res = max(res,nums[i])
            print(res)
        return res
# Answer 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)