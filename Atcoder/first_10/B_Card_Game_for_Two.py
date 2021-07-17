N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
alice=0
bob=0
for i in range(N):
  if i%2==0:
    alice+=A[i]
  else:
    bob+=A[i]
print(alice-bob)

# answer
N = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[::2])-sum(a[1::2]))