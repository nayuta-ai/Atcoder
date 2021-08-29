S = input()
v = 0
m = 0
l = ['A','C','G','T']
for i in range(len(S)):
  if S[i] in l:
    v = v + 1
    m = max(v,m)
  else:
    v = 0
print(m)