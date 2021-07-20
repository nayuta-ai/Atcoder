N = int(input())
restaurant = []
for i in range(N):
  s,p = input().split()
  restaurant.append((s.strip(),int(p)))
rank = sorted(restaurant,key=lambda x : (x[0], -x[1]))
for a in rank:
  print(int(restaurant.index(a))+1)