n,d = map(int,input().split())
m = d*2+1
if n%m==0:
  print(int(n/m))
else:
  print(int(n/m)+1)