n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
  if b[i] > a[i]:
    if a[i]+a[i+1] < b[i]:
      cnt+=a[i]+a[i+1]
      a[i+1] = 0
    else:
      cnt+=b[i]
      a[i+1]-=b[i]-a[i]
  else:
    cnt+=b[i]
print(cnt)