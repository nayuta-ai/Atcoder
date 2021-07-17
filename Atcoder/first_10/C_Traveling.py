# answer
N = int(input())
count=0
px = 0
py = 0
pt = 0
for i in range(N):
  t,x,y=map(int,input().split())
  if (abs(x-px)+abs(y-py))<= t-pt and t%2==(x+y)%2:
    count+=1
  pt=t
  px=x
  py=y
print('Yes'if count==N else "No")