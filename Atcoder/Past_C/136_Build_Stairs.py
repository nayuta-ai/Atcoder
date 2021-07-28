n = int(input())
h = list(map(int,input().split()))
ans = "Yes"
st = h[0]-1
for i in range(n):
  if h[i]<st:
    ans = "No"
    break;
  if st < h[i]-1:
    st = h[i]-1
print(ans)