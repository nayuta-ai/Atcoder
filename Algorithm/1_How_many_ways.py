# yuta
bool = True
while bool:
  cnt = 0
  n , x = map(int,input().split())
  if n==0 and x==0:
    break;
  for i in range(n):
    for j in range(i+1,n):
      ans = x-(i+1)-(j+1)
      if ans > j+1 and ans <= n:
        cnt += 1
  print(cnt)
# kobashuu
output_list = []
while True:
    num_list = list(map(int, input().split()))
    if num_list == [0, 0]:
        break
    output = 0
    for i in range(1, num_list[1]//3):
        for j in range(i + 1, num_list[1]//2):
            k = num_list[1] - i - j
            if j < k and k <= num_list[0]:
                output += 1
    output_list.append(output)

for ans in output_list:
    print(ans)