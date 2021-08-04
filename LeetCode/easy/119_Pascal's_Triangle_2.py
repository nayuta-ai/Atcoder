import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        list = []
        for i in range(0,rowIndex+1):
            list.append(combinations_count(rowIndex,i))
        return list