N = int(input())
S = input()
cnt = 0
for i in range(1000):
  V = str(i).zfill(3)
  p = -1
  for j in range(3):
    p = S.find(V[j],p+1)
    if p == -1:
      break;
    if j == 2:
      cnt = cnt + 1
print(cnt)