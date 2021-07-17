N,A,B = map(int,input().split())
sum=0
for i in range(1,N+1):
  a=i%10+int(i%100/10)+int(i%1000/100)+int(i%10000/1000)+int(i/10000)
  if A<=a and a<=B:
    sum+=i
print(sum)
# Answer
N, A, B = map(int, input().split())
print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))