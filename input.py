# str input
s = input()
# int input
s = int(input())
# (1,N)data
## str
a,b,c,...,n = input().split()
l = input().split() # list
## int
a,b,c,...,n = map(int,input().split())
l = list(map(int,input().split())) # l[i]
# (N,1)data
A = [int(input()) for _ in range(M)]
# (N,M)data
## x[i],y[i]
l = [list(map(int, input().split())) for l in range(N)]
# int,str
list = []
for i in range(N):
    a,b=input().split()
    list.append([int(a), b])