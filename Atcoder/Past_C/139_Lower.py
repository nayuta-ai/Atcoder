n = int(input())
h = list(map(int,input().split()))
cnt = 0
max = 0
for i in range(n-1):
  if h[i] >= h[i+1]:
    cnt += 1
    if cnt > max:
      max = cnt
  else:
    cnt = 0
print(max)