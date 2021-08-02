n = int(input())
b = list(map(int,input().split()))
sum = b[0]
for i in range(n-2):
  if b[i] <= b[i+1]:
    sum+=b[i]
  else:
    sum+=b[i+1]
sum += b[n-2]
print(suｍ)