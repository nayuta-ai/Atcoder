N = int(input())
X = list(map(int,input().split()))
count = 0
while all(a%2==0 for a in X):
  X = [a/2 for a in X]
  count+=1
print(count)