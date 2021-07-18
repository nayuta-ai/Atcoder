import math
N,K = map(int,input().split())
sum = 0

def count(i,K):
  q = math.log2(K/i)
  if int(q)==q:
    return q
  else:
    return int(q)+1

if K <= N:
  for i in range(1,K):
    q = count(i,K)
    sum+=round((1-math.pow(0.5,q))/N,13)
  print(round(1-sum,12))
else:
  for i in range(1,N+1):
    q = count(i,K)
    sum+=round(math.pow(0.5,q)/N,13)
  print(round(sum,12))