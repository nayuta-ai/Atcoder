n = int(input())
p = list(map(int,input().split()))
bull = True
if p == sorted(p):
  print("YES")
else:
  for i in range(n):
    for j in range(i+1,n):
      p[i],p[j]=p[j],p[i]
      if p == sorted(p):
        print("YES")
        bull = False
        break;
      p[i],p[j]=p[j],p[i]
  if bull:
    print("NO")