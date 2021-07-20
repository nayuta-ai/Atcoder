N,M = map(int,input().split())
bulbs=[]
for i in range(M):
  x = tuple(map(int,input().split()))
  bulbs.append(x[1:])
p = list(map(int,input().split()))
ans = 0
for i in range(2**N):
  check=[0]*M
  for j,bulb in enumerate(bulbs):
    cnt=0
    for b in bulb:
      if i >> (b-1) & 1:
        cnt += 1
    if cnt % 2 == p[j]:
      check[j] = True
    else:
      check[j] = False
  if all(check):
    ans += 1
print(ans)