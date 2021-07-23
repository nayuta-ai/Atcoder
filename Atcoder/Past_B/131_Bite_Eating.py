n,l = map(int,input().split())
ans = [0]*n
ref = [0]*n
for i in range(1,n+1):
  ans[i-1]=i+l-1
  ref[i-1]=abs(i+l-1)
a=ref.index(min(ref))
ans.pop(a)
print(sum(ans))