# 動的計画法(DP)
n,m = map(int,input().split())
a=[0]*m
min=[0]*m
max=[0]*m
MOD = 10**9 + 7
for i in range(m):
  a[i]=int(input())
is_safe = [True] * (n+2)
for i in a:
  is_safe[i+1]=False
dp = [0]*(n+2)
dp[1]=1
for i in range(2,n+2):
  if is_safe[i]:
    dp[i] = dp[i-1] + dp[i-2]
    dp[i]%=MOD
  else:
    dp[i]=0
print(dp[n+1])