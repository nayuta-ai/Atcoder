SM = []
SN = []
m = int(input())
for i in range(m):
  x,y = map(int,input().split())
  SM.append((x,y))
n = int(input())
for i in range(n):
  x,y = map(int,input().split())
  SN.append((x,y))
base = SM[0]
for sn in SN:
  dx,dy = sn[0]-base[0], sn[1]-base[1]
  flag = True
  for sm in SM:
    if not(sm[0]+dx,sm[1]+dy) in SN:
      flag = False
      break
  if flag:
    print(dx,dy)
    exit()