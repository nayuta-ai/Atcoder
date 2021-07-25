l,r = map(int,input().split())
INF = 100000000
MOD = 2019
ans = INF
for i in range(l,min(l+MOD,r+1)):
  for j in range(i+1,min(l+MOD,r+1)):
    ans = min(ans,((i%MOD)*(j%MOD))%MOD)
print(ans)