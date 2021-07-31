n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(n):
  if i == 0:
    a[i]=a[i]/2**(n-1)
  else:
    a[i]=a[i]/2**(n-i)
print(sum(a))