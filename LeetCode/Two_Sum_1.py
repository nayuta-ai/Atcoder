class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in hashmap:
                return [hashmap[num],i]
            else:
                hashmap[complement]=i