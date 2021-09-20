N = int(input())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
# 中央値を入口、出口とする
am = A[N//2]
bm = B[N//2]

ans = 0
for a,b in zip(A,B):
    ans += abs(a-b) # AからB
    ans += abs(a-am) # 入口からA
    ans += abs(b-bm) # 出口からB
print (ans)