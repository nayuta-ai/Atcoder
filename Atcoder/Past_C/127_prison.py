# O(n^2)
N,M = map(int,input().split())
for i in range(M):
  l,r=map(int,input().split())
  a = range(l,r+1)
  if i==0:
    b=a
  b = set(b) & set(a)
print(len(b))
# Answer O(n)
N,M = map(int,input().split())
l=[0]*M
r=[0]*M
for i in range(M):
  l[i],r[i]=map(int,input().split())
  if i == 0:
    ans = len(range(l[i],r[i]+1))
  else:
    if l[i-1] > l[i]:
      l[i]=l[i-1]
    if r[i-1] < r[i]:
      r[i]=r[i-1]
  ans = min(ans,len(range(l[i],r[i]+1)))
print(ans)