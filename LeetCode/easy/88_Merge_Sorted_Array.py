class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        for i in range(n):
            nums1.remove(0)
        nums1.sort()
        return nums1