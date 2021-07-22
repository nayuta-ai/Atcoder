w,h,x,y = map(int,input().split())
cnt = 0
if x*2 == w and y*2== h:
  cnt+=1
print(w*h/2,cnt)