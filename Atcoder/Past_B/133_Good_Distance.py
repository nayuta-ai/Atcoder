import math
n,d = map(int,input().split())
x = [list(map(int, input().split())) for x in range(n)]
cnt = 0
for i in range(n):
  for j in range(i+1,n):
    sum = 0
    for l in range(d):
      sum+=(x[i][l]-x[j][l])**2
    sum = math.sqrt(sum)
    if sum == int(sum):
      cnt+=1
print(cnt)