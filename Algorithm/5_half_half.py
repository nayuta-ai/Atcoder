# solution
A,B,C,X,Y = map(int,input().split())
ans = 2*5000*10**5
for Z in range(2*10**5+1):
  total = max(X-Z,0)*A+max(Y-Z,0)*B+2*C*Z
  ans = min(ans,total)
print(ans)

# other solution
A,B,C,X,Y = map(int,input().split())
a = A*X + B*Y
if X > Y:
  b = min(C*2*X,C*2*Y+A*(X-Y))
else:
  b = min(C*2*Y,C*2*X+B*(Y-X))
output = min(a,b)
print(output)