class Solution:
    def mySqrt(self, x: int) -> int:
        f = 0
        while f * f <= x:
            ans = f
            f += 1
        return ans

# Binary Search (https://www.codereading.com/algo_and_ds/algo/binary_search.html)
class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1