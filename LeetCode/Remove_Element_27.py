class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = nums.count(val)
        for i in range(num):
            nums.remove(val)