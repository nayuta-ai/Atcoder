N,M = map(int,input().split())
A = [list(map(int, input().split())) for A in range(N)]
m = 0
for i in range(M):
  for j in range(i+1,M):
    v = 0
    for k in range(N):
      v = max(A[k][i],A[k][j]) + v
    m = max(v,m)
print(m)