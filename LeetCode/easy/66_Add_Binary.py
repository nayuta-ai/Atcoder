class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a)+int(b)
        cnt = 0
        ans = []
        for i in reversed(str(c)):
            h = int(i)+cnt
            cnt = 0
            print(h)
            if h > 1:
                ans.append(h-2)
                cnt+=1
            else:
                ans.append(h)
        if cnt == 1:
            ans.append(1)
        ans.reverse()
        return "".join(map(str,ans))