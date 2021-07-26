n = int(input())
A = [int(input()) for _ in range(n)]
max_value = max(A)
max_index = A.index(max_value)
for i in range(n):
  if i==max_index:
    A.pop(max_index)
    print(max(A))
  else:
    print(max_value)