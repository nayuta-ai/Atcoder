n = int(input())
w = list(map(int,input().split()))
min = 100
for i in range(n):
  s1 = sum(w[:i+1])
  s2 = sum(w[i+1:])
  if abs(s1-s2) < min:
    min = abs(s1-s2)
print(min)