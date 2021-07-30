k,n = map(int,input().split())
L = list(range(n-k+1,k+n))
L=[str(a) for a in L]
L = ' '.join(L)
print(L)